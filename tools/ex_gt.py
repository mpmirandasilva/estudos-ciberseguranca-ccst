# Exercícios da trilha "Gerenciamento de Ameaças Cibernéticas"
# mc: a primeira opção é a correta (o site embaralha). in: resposta digitada. multi: vários campos.
def mc(q,o,e,r): return {'t':'mc','q':q,'o':o,'e':e,'r':r}
def inp(q,a,n,e,r,ph=None,d=None):
    x={'t':'in','q':q,'a':a,'n':n,'e':e,'r':r}
    if ph: x['ph']=ph
    if d: x['d']=d
    return x
def multi(q,f,e,r): return {'t':'multi','q':q,'f':f,'e':e,'r':r}
def C(l,ch,a): return {'l':l,'ch':ch,'a':a}
def assoc(q,pairs,e,r):
    ch=[b for _,b in pairs]
    return multi(q,[C(a,ch,b) for a,b in pairs],e,r)

EX={}
EX[1]=[
 mc('Qual é a diferença entre governança e gerenciamento de segurança de TI?',
    ['A governança decide quem toma as decisões sobre os riscos; o gerenciamento define e implementa os controles','A governança instala firewalls; o gerenciamento cria leis','São a mesma coisa','A governança só trata de backups'],
    'A governança decide; o gerenciamento executa.','1.1'),
 assoc('Associe cada função da governança de dados.',[
    ('Proprietário dos dados','Atribui a classificação e define os critérios de acesso'),
    ('Custodiante dos dados','Implementa a classificação e os controles técnicos'),
    ('Controlador dos dados','Define para que e de que forma os dados pessoais são tratados'),
    ('Processador dos dados','Trata dados pessoais em nome do controlador')],
    'O DPO supervisiona a estratégia de proteção de dados.','1.1'),
 assoc('Classifique cada política.',[
    ('Política de Segurança Cibernética','Mestra'),
    ('Como configurar a política do firewall','Específica do sistema'),
    ('Uso aceitável de e-mail e internet','Específica do problema')],
    'A política mestra é o plano estratégico do programa de segurança.','1.2'),
 mc('Qual política define como relatar e responder a incidentes de segurança?',
    ['Tratamento de incidentes','Manutenção de rede','Acesso remoto','Credenciais'],
    'As políticas precisam ser claras, conhecidas por todos e apoiadas pela alta gerência.','1.3'),
]
EX[2]=[
 assoc('Associe cada perspectiva ética ao seu princípio.',[
    ('Utilitarista','O maior bem para o maior número de pessoas'),
    ('Dos direitos','Cada pessoa tem o direito de fazer as próprias escolhas'),
    ('Do bem comum','Ações que beneficiam toda a comunidade')],
    'A ética utilitarista foi formulada por Bentham e Mill.','2.1'),
 assoc('Classifique cada crime cibernético.',[
    ('Um ataque DoS a um site','Contra o computador'),
    ('Uma fraude bancária online','Assistido por computador'),
    ('Um computador que guarda registros de tráfico','Incidental ao computador')],
    'O que muda é o papel do computador: alvo, ferramenta ou depósito de informações.','2.3'),
 assoc('Associe cada lei americana ao que ela protege.',[
    ('COPPA','Privacidade de crianças menores de 13 anos'),
    ('FERPA','Registros escolares dos estudantes'),
    ('HIPAA','Informações de saúde'),
    ('GLBA','Informações financeiras compartilhadas em transações')],
    'Os EUA não têm uma lei federal central de privacidade, mas um conjunto de leis.','2.7'),
 mc('Qual lei americana proíbe o acesso não autorizado a sistemas de computador?',
    ['CFAA','ECPA','FOIA','VPPA'],
    'A CFAA, de 1986, também torna crime traficar senhas e transmitir código que cause dano.','2.6'),
 mc('Qual é a lei brasileira de proteção de dados pessoais?',
    ['LGPD','GDPR','SOX','PCI DSS'],
    'A LGPD (Lei 13.709/2018) usa os papéis de controlador, operador e encarregado.','2.7'),
]
EX[3]=[
 mc('Como o modelo ISO 27000 descreve as categorias de segurança?',
    ['Por domínios, em um modelo não hierárquico','Por camadas, como o modelo OSI','Por portas TCP','Por tipos de malware'],
    'Cada domínio se relaciona diretamente com os outros.','3.2'),
 mc('Qual é a diferença entre a ISO 27001 e a ISO 27002?',
    ['A 27001 traz os objetivos de controle; a 27002, os controles que dizem como atingi-los','A 27001 é sobre redes sem fio; a 27002, sobre nuvem','A 27002 substitui a 27001','Não há diferença'],
    'Passar na auditoria da 27001 mostra que a empresa está em conformidade.','3.3'),
 mc('Qual documento adapta os controles da ISO 27000 às prioridades da empresa?',
    ['A declaração de aplicabilidade (SOA)','O relatório SOC 2','A matriz CCM','O CVE'],
    'A SOA ajusta os controles às prioridades de confidencialidade, integridade e disponibilidade.','3.4'),
 mc('Quantos objetivos de controle e domínios tem a matriz de controles de nuvem (CCM) da CSA?',
    ['197 objetivos em 17 domínios','12 objetivos em 7 domínios','18 objetivos em 3 domínios','100 objetivos em 10 domínios'],
    'A CCM é considerada o padrão de fato da segurança na nuvem.','3.7'),
 mc('Qual é a diferença entre o relatório SOC 2 Tipo I e o Tipo II?',
    ['O Tipo I confirma os controles em um momento; o Tipo II, por pelo menos seis meses','O Tipo I é para nuvem; o Tipo II, para redes','O Tipo II é mais barato','Não há diferença'],
    'São auditorias independentes dos controles de um provedor.','3.8'),
]
EX[4]=[
 inp('Um servidor de US$ 15.000 tem EF de 100% e ARO de 15%. Qual é a ALE, em dólares?',['2250','2.250'],'num',
    'SLE = 15.000 × 1,0 = 15.000; ALE = 15.000 × 0,15 = 2.250.','4.5.2',ph='US$'),
 inp('Um ativo de US$ 40.000 perde metade do valor em um ataque que ocorre uma vez a cada cinco anos. Qual é a ALE, em dólares?',['4000','4.000'],'num',
    'SLE = 40.000 × 0,5 = 20.000; ARO = 0,2; ALE = 20.000 × 0,2 = 4.000.','4.5.1',ph='US$'),
 mc('Uma proteção custa US$ 15.000 por ano e o risco tem ALE de US$ 12.000. Ela compensa?',
    ['Não, porque custa mais que a perda anual esperada','Sim, sempre','Sim, porque toda proteção compensa','Não dá para saber'],
    'O custo da contramedida não deve ser maior que o valor que ela protege.','4.2'),
 assoc('Classifique cada fonte de ameaça.',[
    ('Um incêndio','Ambiental'),
    ('Um funcionário que apaga um arquivo por engano','Acidental'),
    ('Um grupo de hackers','Adversarial'),
    ('Um disco que queima','Estrutural')],
    'As fontes podem ser internas ou externas.','4.3'),
 assoc('Associe cada ação à resposta ao risco.',[
    ('Contratar um seguro','Transferir'),
    ('Deixar de oferecer um serviço vulnerável','Evitar'),
    ('Instalar um firewall','Reduzir'),
    ('Conviver com um risco de baixo impacto','Aceitar')],
    'Um bom plano pode combinar duas ou mais estratégias.','4.6'),
 mc('Qual atitude deixa o risco em nível aceitável?',
    ['Devida diligência','Negligência','Devido cuidado','Nenhuma'],
    'Negligência → risco alto; devido cuidado → menor; devida diligência → aceitável.','4.1'),
]
EX[5]=[
 assoc('Classifique cada controle pela função.',[
    ('Backup e restauração','Recuperação'),
    ('Câmera visível na entrada','Dissuasivo'),
    ('IDS','De detecção'),
    ('Privilégios específicos por usuário','Preventivo'),
    ('Detector de movimento com som de latidos no lugar de um cão','Compensatório')],
    'A dissuasão desencoraja, a prevenção impede, a detecção descobre depois e a correção e a recuperação consertam.','5.2'),
 mc('O que é o risco inerente?',
    ['O risco que o sistema representa por si só, sem controles','O risco que sobra depois dos controles','O risco transferido a uma seguradora','O risco de um desastre natural'],
    'Os controles reduzem o risco inerente.','5'),
 assoc('Classifique cada controle pelo tipo de implementação.',[
    ('Política de senhas','Administrativo'),
    ('Firewall','Técnico'),
    ('Cerca e fechadura','Físico')],
    'Os administrativos determinam como as pessoas agem.','5.1'),
]
EX[6]=[
 mc('O que o CVE oferece?',
    ['Um identificador único para cada vulnerabilidade conhecida','Uma nota de gravidade de 0 a 10','Um antivírus gratuito','Um curso de segurança'],
    'O CVE é mantido pela MITRE e facilita o compartilhamento de dados.','6.4'),
 mc('Qual é a diferença entre STIX e TAXII?',
    ['O STIX é o formato da informação; o TAXII é o protocolo que a transporta sobre HTTPS','O TAXII é o formato; o STIX, o transporte','Os dois são antivírus','São nomes da mesma coisa'],
    'O CybOX foi incorporado ao STIX.','6.5'),
 mc('Qual serviço gratuito do DHS troca indicadores de ameaças em tempo real com o setor privado?',
    ['AIS','MISP','Cisco Talos','FireEye Helix'],
    'Assim que uma ameaça é reconhecida, ela é compartilhada com a comunidade.','6.3'),
 mc('Quais são os três tipos de dados de uma plataforma de inteligência de ameaças (TIP)?',
    ['IOCs, TTPs e informações de reputação','Senhas, usuários e grupos','Logs, backups e patches','IPs, MACs e portas'],
    'A TIP centraliza dados de várias fontes e os apresenta de forma utilizável.','6.6'),
 mc('Por que é vantajoso colocar um honeypot na nuvem?',
    ['Isola o honeypot das redes de produção','Deixa o honeypot mais rápido','Dispensa monitoramento','Bloqueia todos os ataques'],
    'Hospedar honeypots é arriscado; na nuvem, eles ficam separados da rede real.','6.6'),
]
EX[7]=[
 mc('Por que os picos de uso durante os backups entram na linha de base da rede?',
    ['Porque fazem parte da operação normal','Porque são ataques','Porque a lei exige','Porque não são medidos'],
    'Já o tráfego de um servidor que foi para a nuvem deixou de ser normal e sai da linha de base.','7.1'),
 mc('O que pode indicar um aumento do tráfego entre clientes da rede?',
    ['Malware se espalhando lateralmente','Um backup normal','Uma atualização do Windows','Um usuário imprimindo'],
    'Os clientes costumam falar com servidores, não entre si.','7.1'),
 inp('Com X = 10, Y = 50, Z = 20 e N = 300, uma amostra registra 350 fluxos. Digite 1 se gera alarme ou 0 se não gera.',['1'],'num',
    '350 > 300, então o algoritmo gera o alarme.','7.3.1',ph='1 ou 0'),
 mc('O que é o perfil de servidor?',
    ['A linha de base de segurança de um servidor específico','O nome do servidor no DNS','A lista de usuários da empresa','O modelo do hardware'],
    'Define portas de escuta, contas, contas de serviço e software permitidos.','7.2'),
]
EX[8]=[
 mc('Qual é a diferença entre avaliação de vulnerabilidades e teste de penetração?',
    ['A avaliação encontra os pontos fracos; o teste de penetração os explora','A avaliação é ilegal','O teste de penetração só usa antivírus','São a mesma coisa'],
    'O pen test usa ataques simulados autorizados para medir o impacto.','8.1'),
 mc('Qual varredura gera menos falsos positivos e falsos negativos?',
    ['Credenciada','Não credenciada','Invasiva sem senha','Nenhuma'],
    'Com usuário e senha, o scanner coleta mais informações.','8.2'),
 assoc('Associe cada erro do scanner.',[
    ('Falso positivo','Aponta uma vulnerabilidade que não existe'),
    ('Falso negativo','Não aponta uma vulnerabilidade que existe')],
    'Por isso é preciso analisar logs e configurações antes de agir.','8.2'),
 mc('Quando o ST&E é realizado?',
    ['Com a rede totalmente integrada e em operação','Antes de comprar os equipamentos','Só depois de um ataque','Nunca, é opcional'],
    'O ST&E examina as proteções de uma rede em operação.','8.4'),
]
EX[9]=[
 assoc('Associe cada comando ao que ele faz.',[
    ('netstat','Mostra as portas em escuta e as conexões ativas'),
    ('tracert','Rastreia a rota de um pacote'),
    ('nslookup','Consulta um servidor DNS'),
    ('arp','Mostra a tabela que associa MAC e IP')],
    'No Linux, os equivalentes de tracert e nslookup são traceroute e dig.','9.1'),
 mc('Qual é a diferença entre a varredura de portas e a varredura de hosts (port sweeping) do Nmap?',
    ['A primeira procura vários serviços em um host; a segunda, o mesmo serviço em vários hosts','São iguais','A primeira usa UDP e a segunda TCP','A segunda só funciona no Windows'],
    'O Nmap também faz varreduras furtivas e identifica o sistema operacional.','9.3'),
 mc('Qual função do SIEM reduz o volume de eventos?',
    ['Agregação','Correlação','Retenção','Análise forense'],
    'A agregação consolida registros duplicados; a correlação liga eventos de sistemas diferentes.','9.5'),
 mc('O que o SOAR faz?',
    ['Coleta dados de ameaças e responde a eventos de nível mais baixo sem intervenção humana','Substitui o firewall','Distribui endereços IP','Faz backup dos servidores'],
    'O SOAR pode ser integrado ao SIEM.','9.6'),
]
EX[10]=[
 assoc('Associe cada tipo de teste de penetração ao conhecimento do especialista.',[
    ('Caixa preta','Nenhum conhecimento do sistema'),
    ('Caixa cinza','Conhecimento limitado'),
    ('Caixa branca','Conhecimento completo')],
    'A caixa preta é a mais barata; a branca, a mais cara.','10.1'),
 mc('Qual é a ordem das fases de um teste de penetração?',
    ['Planejamento, descoberta, ataque e relatório','Ataque, descoberta, planejamento e relatório','Relatório, ataque, descoberta e planejamento','Descoberta, relatório, ataque e planejamento'],
    'No planejamento são definidas as regras de engajamento.','10.2'),
 assoc('Associe cada equipe ao seu papel no exercício.',[
    ('Vermelha','Ataca sem ser percebida'),
    ('Azul','Defende'),
    ('Branca','Árbitro neutro'),
    ('Roxa','Vermelha e azul trabalhando juntas')],
    'A equipe branca conhece governança e conformidade.','10.3'),
 mc('Como se chama o reconhecimento feito sem interagir com o alvo?',
    ['Footprinting (passivo)','Varredura de portas','Pivoting','Persistência'],
    'O reconhecimento ativo, como a varredura de portas, interage com o alvo.','10.2'),
]
EX[11]=[
 assoc('Classifique cada nota CVSS.',[
    ('3,9','Baixa'),('4,0','Média'),('7,5','Alta'),('9,8','Crítica')],
    'Baixa 0,1–3,9; média 4,0–6,9; alta 7,0–8,9; crítica 9,0–10,0.','11.5'),
 mc('Em geral, a partir de que nota uma vulnerabilidade deve ser corrigida?',
    ['Acima de 3,9','Acima de 9,0','Só se for 10','Acima de 0,1'],
    'Quanto maior a nota, maior a urgência.','11.5'),
 mc('Qual grupo de métricas do CVSS precisa ser preenchido primeiro?',
    ['Base','Temporal','Ambiental','Qualquer um'],
    'As métricas temporais e ambientais modificam a nota base.','11.4'),
 mc('Na string CVSS, o que significa AV:N?',
    ['Vetor de ataque pela rede','Disponibilidade nenhuma','Autenticação necessária','Ataque virtual'],
    'Os valores de AV são N (rede), A (adjacente), L (local) e P (físico).','11.4'),
 mc('Quem completa o grupo de métricas ambientais?',
    ['A empresa afetada','O fornecedor','O FIRST','O NIST'],
    'O fornecedor informa as notas base e temporal.','11.5'),
 mc('O que o NVD acrescenta ao CVE?',
    ['Notas CVSS, detalhes técnicos e entidades afetadas','Antivírus','Senhas padrão','Endereços IP dos atacantes'],
    'O NVD é mantido pelo NIST.','11.6'),
]
EX[12]=[
 mc('Qual é a ordem do ciclo de vida do gerenciamento de vulnerabilidades?',
    ['Descobrir, priorizar ativos, avaliar, relatar, corrigir e verificar','Corrigir, descobrir, relatar e verificar','Avaliar, corrigir e descobrir','Relatar, verificar e descobrir'],
    'A verificação usa auditorias de acompanhamento.','12.1'),
 mc('Como os administradores devem considerar os dispositivos móveis?',
    ['Não confiáveis até que a empresa os proteja','Sempre confiáveis','Confiáveis se forem novos','Confiáveis se tiverem senha'],
    'Eles podem ser perdidos, roubados ou adulterados fora da empresa.','12.3'),
 mc('Qual técnica de aplicação de patches é a preferida para dispositivos móveis?',
    ['Baseada em agente','Varredura sem agente','Monitoramento passivo','Instalação manual'],
    'O agente fala com o servidor de patches mesmo fora dos segmentos varridos.','12.5'),
 mc('Do que o gerenciamento de patches depende para saber quais sistemas corrigir?',
    ['Dos dados do gerenciamento de ativos','Do SIEM','Do firewall','Do servidor DNS'],
    'Sem inventário, não se sabe o que precisa de patch.','12.5'),
 mc('Quais ferramentas gerenciam a configuração de muitos servidores na nuvem?',
    ['Puppet, Chef, Ansible e SaltStack','Nmap e Wireshark','Snort e Suricata','Nessus e Qualys'],
    'Para equipamentos de rede, há ferramentas que fazem backup e detectam alterações das configurações.','12.4'),
]
EX[13]=[
 mc('Qual é a ordem das etapas da Cyber Kill Chain?',
    ['Reconhecimento, armamento, entrega, exploração, instalação, comando e controle, ações nos objetivos','Entrega, reconhecimento, instalação, exploração, armamento, ações e C2','Armamento, reconhecimento, entrega, C2, exploração, instalação e ações','Exploração, entrega, reconhecimento, armamento, instalação, ações e C2'],
    'Se o atacante for parado em qualquer etapa, a cadeia se rompe.','13.1'),
 assoc('Associe cada ação à etapa da Cyber Kill Chain.',[
    ('Webshell instalado no servidor','Instalação'),
    ('E-mail com anexo malicioso','Entrega'),
    ('Varredura de portas do alvo','Reconhecimento'),
    ('Tráfego excessivo para um domínio de DNS dinâmico','Comando e controle')],
    'Quanto mais cedo o ataque é parado, menor o dano.','13.1'),
 mc('Qual etapa é a última chance de bloquear a operação do atacante?',
    ['Comando e controle','Reconhecimento','Armamento','Entrega'],
    'Depois do C2, o atacante age nos objetivos e fica difícil de remover.','13.7'),
 mc('O que é um ataque de dia zero na etapa de armamento?',
    ['Uma arma desconhecida pelos defensores e pelos sistemas de segurança','Um ataque já conhecido','Um backup','Um teste autorizado'],
    'Ataques conhecidos são mais fáceis de detectar pelos defensores.','13.3'),
]
EX[14]=[
 mc('Quais são os quatro elementos do Modelo Diamond?',
    ['Adversário, capacidade, infraestrutura e vítima','Ameaça, risco, controle e ativo','Coleta, exame, análise e relatório','Preparação, detecção, contenção e pós-incidente'],
    'O adversário usa a infraestrutura para se conectar à vítima e desenvolve a capacidade para explorá-la.','14.1'),
 mc('No Modelo Diamond, o que é a infraestrutura?',
    ['Os caminhos de rede usados para manter o comando e controle','A ferramenta usada no ataque','O alvo do ataque','O grupo responsável'],
    'A capacidade é a ferramenta ou técnica.','14.1'),
 mc('Qual meta-recurso do Modelo Diamond equivale às etapas da Cyber Kill Chain?',
    ['Fase','Direção','Metodologia','Resultado'],
    'A atividade maliciosa tem duas ou mais fases sucessivas.','14.2'),
]
EX[15]=[
 mc('Qual é a ordem do processo forense da NIST SP 800-86?',
    ['Coleta, exame, análise e relatório','Análise, coleta, relatório e exame','Exame, coleta, análise e relatório','Relatório, análise, exame e coleta'],
    'Mídia vira dados, dados viram informações e informações viram evidências.','15.2'),
 mc('Segundo a RFC 3227, qual evidência deve ser coletada primeiro?',
    ['A mais volátil, como a RAM e os caches','O backup em fita','O disco rígido','A topologia física'],
    'A coleta vai da evidência mais volátil para a menos volátil.','15.4'),
 mc('Por que a análise forense é feita em cópias bit a bit?',
    ['Para não alterar a prova original e poder provar que não houve adulteração','Porque é mais rápido','Porque o original é apagado','Porque a lei proíbe cópias'],
    'Abrir arquivos da mídia original altera os carimbos de hora.','15.6'),
 mc('Qual tipo de evidência, junto com outros fatos, sustenta uma hipótese?',
    ['Indireta (circunstancial)','Melhor evidência','Direta','Corroborativa'],
    'Semelhanças de TTPs com atacantes conhecidos são evidência circunstancial.','15.3'),
 mc('O que o MITRE ATT&CK descreve?',
    ['O comportamento do atacante, em táticas, técnicas e procedimentos','O código-fonte dos malwares','As leis de cada país','As notas CVSS'],
    'É uma base de conhecimento global feita a partir de explorações reais.','15.8'),
]
EX[16]=[
 mc('Qual é a ordem das fases do ciclo de resposta a incidentes do NIST?',
    ['Preparação, detecção e análise, contenção/erradicação/recuperação, atividade pós-incidente','Detecção, preparação, recuperação e contenção','Contenção, detecção, preparação e pós-incidente','Pós-incidente, preparação, detecção e contenção'],
    'O ciclo é um processo de aprendizado que se reforça.','16.4'),
 assoc('Associe cada sinal ao que ele indica.',[
    ('Precursor','Um incidente pode ocorrer no futuro'),
    ('Indicador','Um incidente já ocorreu ou está ocorrendo')],
    'Exemplo de precursor: log de resposta a uma varredura; de indicador: alerta do IDS.','16.6'),
 mc('Por que nem sempre convém desconectar da rede um host comprometido?',
    ['O malware pode perceber a perda do C2 e apagar ou criptografar os dados','Porque a rede cai inteira','Porque o host para de funcionar para sempre','Porque a lei proíbe'],
    'A experiência da equipe ajuda a escolher a estratégia de contenção.','16.7'),
 mc('O que é o kit de salto (jump kit)?',
    ['Uma caixa portátil com o necessário para uma resposta rápida','Um curso de treinamento','Um tipo de malware','Um relatório pós-incidente'],
    'Ele deve ser inspecionado regularmente e usado em treinos.','16.5'),
 mc('Qual fase pode ser a mais difícil da resposta a incidentes?',
    ['Detecção','Preparação','Recuperação','Atividade pós-incidente'],
    'Alguns incidentes passam despercebidos por meses.','16.6'),
 mc('Quantos níveis tem o domínio de resposta a incidentes do CMMC?',
    ['Quatro','Cinco','Três','Dois'],
    'A maioria dos domínios tem cinco níveis, mas a resposta a incidentes tem quatro (do 2 ao 5).','16.3'),
]
EX[17]=[
 assoc('Associe cada medida da BIA.',[
    ('RTO','Tempo máximo tolerável de indisponibilidade'),
    ('RPO','Quantidade máxima de dados que se tolera perder'),
    ('MTTR','Tempo médio para consertar'),
    ('MTBF','Tempo médio entre falhas')],
    'O RPO define a frequência mínima dos backups.','17.3'),
 inp('O RPO de um sistema é de 2 horas. De quantas em quantas horas, no máximo, os backups devem ser feitos?',['2'],'num',
    'Com RPO de 2 horas, não se pode perder mais de 2 horas de dados.','17.3',ph='horas'),
 mc('Qual é a diferença entre o DRP e o BCP?',
    ['O BCP é mais amplo: mantém a empresa funcionando, inclusive em outro local','O DRP é mais amplo que o BCP','São o mesmo plano','O BCP só trata de backups'],
    'O DRP avalia, recupera, repara e restaura os ativos durante o desastre.','17.3'),
 mc('Qual exercício interrompe os serviços para testar todo o plano?',
    ['Exercício operacional','Exercício de mesa','Teste funcional','Nenhum'],
    'No exercício de mesa, nenhum procedimento real é executado.','17.5'),
]
