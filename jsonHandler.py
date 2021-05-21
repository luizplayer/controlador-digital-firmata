import json


class JsonHandler:

    def json_read(self):
        with open('Settings.json', 'r') as json_file:
            self.data = json.load(json_file)

        #Read port settings
        self.textBox1.setText(self.data['AnalogPort'])
        self.textBox2.setText(self.data['PwmPort'])
        self.textBox3.setText(self.data['SampleTime'])

        #adicionar algo para configurar graph range
        self.graphRange = self.data['GraphRange']

        #Read Control settings
        self.textBox4.setText(self.data['OpenLoopGain'])
        self.textBox5.setText(self.data['P'])
        self.textBox6.setText(self.data['I'])
        self.textBox7.setText(self.data['D'])
        self.textBox8.setText(self.data['SP'])
        json_file.close()

    def update_json(self, Ports=None, Control_1=None, Control_2=None):
        if Ports:
            self.data['AnalogPort'] = str(self.analogPort)
            self.data['PwmPort'] = str(self.pwmPort)
            self.data['SampleTime'] = str(self.sampleTime)
            with open('Settings.json', 'w+') as json_file:
                json.dump(self.data, json_file, ensure_ascii=False)
            json_file.close()

        if Control_1:
            self.data['OpenLoopGain']= str(self.pwmValue)
            with open('Settings.json', 'w+') as json_file:
                json.dump(self.data, json_file, ensure_ascii=False)
            json_file.close()

        if Control_2:
            self.data['P']=str(self.kp)
            self.data['I']=str(self.ki)
            self.data['D']=str(self.kd)
            self.data['SP']=str(self.sp)
            with open('Settings.json', 'w+') as json_file:
                json.dump(self.data, json_file, ensure_ascii=False)
            json_file.close()
