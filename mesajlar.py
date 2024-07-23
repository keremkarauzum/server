
hiz=0
enlem=0
boylam=0
irtifa=0
dikilme=0
yonelme=0
yatis=0
hiz=0
batarya=0
def listen_gps(siha):
    @siha.on_message('GPS_RAW_INT')
    def listener(self,name,msg):
        global enlem
        global boylam
        global irtifa
        enlem=msg.lat
        boylam=msg.lon
        irtifa=msg.alt
    return enlem ,boylam,irtifa
def listen_aci(siha):
    @siha.on_message('ATTITUDE')
    def listener(self,name,msg):
        global dikilme
        global yonelme
        global yatis
        yonelme=msg.roll
        dikilme=msg.pitch
        yatis=msg.yaw
    return dikilme,yonelme,yatis

def listen_hiz(siha):
    @siha.on_message('VFR_HUD')
    def listener(self,name,msg):
        global hiz
        hiz=msg.airspeed
    return hiz
def listen_batarya(siha):
    @siha.on_message('SYS_STATUS')
    def listener(self,name,msg):
        global batarya
        batarya=msg.battery_remaining
    return batarya

