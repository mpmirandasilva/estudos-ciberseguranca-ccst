# Ícones em pixel (12x12) da trilha "Gerenciamento de Ameaças Cibernéticas" (reaproveita os desenhos da trilha Defesa de Rede).
import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'icons_def.py')).read().split('\nICONS=')[0])
ICONS={1:BUILD,2:DOC,3:LIST,4:CHART,5:SHIELD,6:EYE,7:WAVE,8:PORTS,9:TERM,10:KEY,11:HASH,12:GEAR,13:CODE,14:ZONES,15:CERT,16:BELL,17:DISKS}
for k,v in ICONS.items():
    assert len(v)==12 and all(len(r)==12 for r in v),k
