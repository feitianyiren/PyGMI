#Multithreading
import threading
#Time measurement
import time

######create a separate thread to run the measurements without freezing the front panel######
class Script(threading.Thread):
    def __init__(self,mainapp,frontpanel,data_queue,stop_flag,Instr_bus_lock,**kwargs):
        #nothing to modify here
        threading.Thread.__init__(self,**kwargs)
        self.mainapp=mainapp
        self.frontpanel=frontpanel
        self.data_queue=data_queue
        self.stop_flag=stop_flag
        self.Instr_bus_lock=Instr_bus_lock
        
    def run(self):
        #this is the part that will be run in a separate thread
        #######################################################
        #SHORTCUTS
        instr=self.mainapp                         #a shortcut to the main app, especially the instruments
        f=self.frontpanel                          #a shortcut to frontpanel values
        reserved_bus_access=self.Instr_bus_lock     #a lock that reserves the access to instruments
        #data_queue=self.data_queue                #a shortcut to a FIFO queue to send the data to the main thread
        #######################################################
        #SAVEFILE HEADER - add column names to this list in the same order as you will send the results of the measurements to the main thread
        #for example if header = ["Time (s)","I (A)","V (volt)"]
        #then you have to send the results of the measurements this way : "self.data_queue.put(([some time, some current, some voltage],False))"
        nb_voltmeter=2
        header=['Time (s)','Time since Epoch']
        if f.temp_controller_on:header+=["T sample (K)","T VTI(K)"]
        voltmeter_is_on=[]
        for i in range(nb_voltmeter):
            if eval("f.instr_on_"+str(i+1)):
                voltmeter_is_on.append(i+1)
                header+=["Vp"+str(i+1),"Vm"+str(i+1),"(Vp"+str(i+1)+"-Vm"+str(i+1)+")/2"]
        
        header+=["Voltage 1 (V)"]
        header+=["Voltage 2 (V)"]
        
        if f.instr_on_14:
            header+=["LHe level (%)"]
            with reserved_bus_access:        
                instr.instr_14.set_unit_to_percent()
                
        #print header

        #######################################################
        #ORIGIN OF TIME FOR THE EXPERIMENT
        start_time=time.clock()
        #######################################################
        #SEND THE HEADER OF THE SAVEFILE BACK TO THE MAIN THREAD, WHICH WILL TAKE CARE OF THE REST
        self.data_queue.put((header,True))

        #######################################################
        #INSTRUMENTS NAMES SHORTCUTS FOR EASIER READING OF THE CODE BELOW
        #I_source=instr.instr_8

        active_voltmeters=[eval("instr.instr_"+str(i)) for i in voltmeter_is_on]
        temp_controller=instr.temp_controller
        temp_controllerVTI=instr.instr_9
        
        #Instruments set-up
        
        for voltmeter in active_voltmeters:
            with reserved_bus_access:
                voltmeter.setup_single_shot()
                voltmeter.set_integration_rate(f.mesure_speed)
        
        #I=f.current1
        voltmeter=instr.instr_1
        voltmeter_res=instr.instr_2
        
        V_source1=instr.instr_5
        V_source2=instr.instr_6                   
        #Instruments set-up
        with reserved_bus_access:
            V_source1.output_OFF()
            V_source1.source_mode('V')
            V_source1.set_current_compliance(f.current1)
            V_source1.set_voltage_source_amplitude(f.voltage1)
            V_source1.output_ON()

            V_source2.output_OFF()
            V_source2.source_mode('V')
            V_source2.set_current_compliance(f.current2)
            V_source2.set_voltage_source_amplitude(f.voltage2)
            V_source2.output_ON()
            
        
        #######################################################
        #MAIN LOOP         
        while True: #loop and measure indefinitely, until the main process tells to stop 
            #Check if the main process is telling to stop
            if self.stop_flag.isSet():
                break

            #Measure T VTI
            with reserved_bus_access:
                T_VTI=temp_controllerVTI.query_temp('A')

            #Measure V              
            nb_active_V=len(active_voltmeters)
            Vp=[0 for j in range(nb_active_V)]
            Vm=[0 for j in range(nb_active_V)]
            with reserved_bus_access:
                T=temp_controller.query_temp('A')/2.0
                #2nd order scheme to correct for the thermoelectric effect 
                #+V
                V_source1.set_voltage_source_amplitude(f.voltage1)
                time.sleep(f.mesure_delay)
                Vp[0]+=voltmeter.query_voltage()/2.0
                Vp[1]+=voltmeter_res.query_voltage()/2.0
                #-V
                V_source1.set_voltage_source_amplitude(-f.voltage1)
                time.sleep(f.mesure_delay)
                Vm[0]+=voltmeter.query_voltage()/2.0
                Vm[1]+=voltmeter_res.query_voltage()/2.0
                V_source1.set_voltage_source_amplitude(-f.voltage1)
                time.sleep(f.mesure_delay)
                Vm[0]+=voltmeter.query_voltage()/2.0
                Vm[1]+=voltmeter_res.query_voltage()/2.0
                #+V
                V_source1.set_voltage_source_amplitude(f.voltage1)
                time.sleep(f.mesure_delay)
                Vp[0]+=voltmeter.query_voltage()/2.0
                Vp[1]+=voltmeter_res.query_voltage()/2.0
                T+=temp_controller.query_temp('A')/2.0
            
            V=[(Vp[j]-Vm[j])/2.0 for j in range(nb_active_V)]
                
            if f.instr_on_14:
                try:
                    with reserved_bus_access:
                        LHe=float(instr.instr_14.query_LHe_level()[:-1])
                except:
                    LHe=-1
            ######Compile the latest data######
            t=time.clock()-start_time
            epochtime=time.time()
            last_data=[t,epochtime]
            last_data.append(T)
            last_data.append(T_VTI)
            for j in range(nb_active_V):
                last_data+=[Vp[j],Vm[j],V[j]]
            last_data.append(f.voltage1)
            last_data.append(f.voltage2)
            if f.instr_on_14:last_data.append(LHe)
            
            #print last_data
            #print map(type,last_data)
            #######Send latest data to the main process for display and storage######
            self.data_queue.put((last_data,False))
            #######Wait mesure_delay secs before taking next measurements
            time.sleep(f.mesure_delay)
        
