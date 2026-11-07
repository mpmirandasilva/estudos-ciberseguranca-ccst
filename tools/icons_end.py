# Ícones em pixel (12x12) da trilha "Segurança de Endpoint" (reaproveita os desenhos da trilha Defesa de Rede).
import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'icons_def.py')).read().split('\nICONS=')[0])
ICONS={1:SHIELD,2:EYE,3:LAYERS,4:USERS,5:SHX,6:DOC,7:PORTS,8:CODE,9:SEGS,10:LIST,11:SERVER,12:FILTER,13:WAVE,14:WIFI,15:LOCKU,
       16:WALL,17:BELL,18:TERM,19:CHIP,20:GEAR,21:KEY,22:TERM,23:SERVER,24:DISKS,25:CODE,26:SHIELD,27:SHX,28:EYE,29:BUILD,30:DOC}
for k,v in ICONS.items():
    assert len(v)==12 and all(len(r)==12 for r in v),k
