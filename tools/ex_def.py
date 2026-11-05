# Exercícios da trilha "Defesa de Rede"
# mc: a primeira opção é a correta (o site embaralha). in: resposta digitada. multi: vários campos.
def mc(q,o,e,r): return {'t':'mc','q':q,'o':o,'e':e,'r':r}
def inp(q,a,n,e,r,ph=None,d=None):
    x={'t':'in','q':q,'a':a,'n':n,'e':e,'r':r}
    if ph: x['ph']=ph
    if d: x['d']=d
    return x
def multi(q,f,e,r): return {'t':'multi','q':q,'f':f,'e':e,'r':r}
def F(l,a,n,d=None,ph=None):
    x={'l':l,'a':a if isinstance(a,list) else [a],'n':n}
    if d: x['d']=d
    if ph: x['ph']=ph
    return x
def C(l,ch,a): return {'l':l,'ch':ch,'a':a}
def assoc(q,pairs,e,r):
    ch=[b for _,b in pairs]
    return multi(q,[C(a,ch,b) for a,b in pairs],e,r)

EX={}
EX[1]=[
 assoc('Associe cada objetivo da tríade CIA ao que ele garante.',[
    ('Confidencialidade','Só pessoas autorizadas leem a informação'),
    ('Integridade','A informação está completa e não foi alterada'),
    ('Disponibilidade','A informação funciona quando é necessária')],
    'Confidencialidade → quem lê; integridade → sem alteração; disponibilidade → acesso quando necessário.','1.1'),
 mc('Um servidor do site da empresa fica fora do ar por causa de um ataque. Qual objetivo da tríade CIA foi afetado?',
    ['Disponibilidade','Confidencialidade','Integridade','Não repúdio'],
    'Serviço fora do ar é falha de disponibilidade.','1.1'),
 mc('Como se chama uma fraqueza em um sistema ou no seu projeto que pode ser explorada?',
    ['Vulnerabilidade','Ameaça','Ativo','Risco residual'],
    'Vulnerabilidade é a fraqueza; ameaça é o perigo potencial para o ativo.','1.2'),
 mc('Qual é o primeiro passo do gerenciamento de ativos?',
    ['Inventariar todos os ativos','Comprar um firewall','Descartar equipamentos antigos','Criptografar todos os discos'],
    'Só é possível proteger o que se conhece: primeiro se inventaria, depois se criam políticas para proteger.','1.3'),
 mc('Em qual etapa do ciclo de vida de um ativo todos os dados precisam ser apagados?',
    ['Descarte','Aquisição','Implantação','Utilização'],
    'No descarte, os dados são apagados e as peças com risco ambiental seguem as regras locais.','1.6'),
]
EX[2]=[
 mc('O que caracteriza a defesa em profundidade?',
    ['Várias camadas de segurança, para que a falha de uma não comprometa as outras','Um único firewall muito potente na borda','Criptografar todos os dados e dispensar outras proteções','Confiar em todos os usuários da rede interna'],
    'A defesa em profundidade usa camadas na borda, dentro da rede e nos dispositivos finais.','2'),
 multi('Coloque as linhas de defesa na ordem em que o tráfego da internet passa por elas.',[
    C('1ª',['Roteador de borda','Firewall','Roteador interno'],'Roteador de borda'),
    C('2ª',['Roteador de borda','Firewall','Roteador interno'],'Firewall'),
    C('3ª',['Roteador de borda','Firewall','Roteador interno'],'Roteador interno')],
    'Internet → roteador de borda → firewall → roteador interno → rede interna.','2.1'),
 mc('Por que a analogia da alcachofra substituiu a da cebola?',
    ['Nas redes sem fronteiras, o atacante só precisa remover algumas folhas para chegar aos dados','Porque a cebola tem menos camadas','Porque a alcachofra representa uma rede sem nenhuma defesa','Porque os firewalls deixaram de existir'],
    'Na cebola, é preciso atravessar todas as camadas; na alcachofra, basta arrancar algumas folhas.','2.2'),
 assoc('Associe cada estratégia de defesa em profundidade ao exemplo.',[
    ('Limitação','Documentos sigilosos só consultados em sala com câmeras'),
    ('Diversidade','Crachá de um fabricante e leitor de digital de outro'),
    ('Ofuscação','Mensagem de erro sem a versão do sistema operacional'),
    ('Simplicidade','Configuração que a equipe entende e mantém corretamente')],
    'As cinco estratégias são sobreposição, limitação, diversidade, ofuscação e simplicidade.','2.3'),
]
EX[3]=[
 mc('O que é o reforço (hardening) do sistema operacional?',
    ['Configurar o sistema de forma segura, reduzindo as brechas que um atacante poderia usar','Instalar mais programas para aumentar a segurança','Trocar o sistema operacional a cada ano','Desativar todas as contas de usuário'],
    'Exemplos de medidas: trocar contas e senhas padrão, aplicar políticas de conta e controlar o acesso aos arquivos.','3.2'),
 mc('Qual é a função de um analisador de pacotes (sniffer)?',
    ['Interceptar e registrar o tráfego da rede','Bloquear pacotes maliciosos','Distribuir endereços IP','Criptografar o tráfego'],
    'Ele captura cada pacote e mostra o valor de cada campo. Exemplos: Wireshark e tcpdump.','3.4'),
 mc('Para que servem os arquivos de log do software de segurança?',
    ['Para auditoria, identificação de tendências e de problemas','Para acelerar a rede','Para guardar as senhas dos usuários','Para substituir o backup'],
    'Os logs registram atividades e permitem investigar o que aconteceu.','3.3'),
 mc('O que faz o gerenciamento de configuração?',
    ['Identifica, controla e audita a implantação dos sistemas e as alterações na linha de base','Monitora os usuários em tempo real','Substitui o inventário de ativos','Cria contas de administrador'],
    'A linha de base é o modelo de configuração para todos os sistemas semelhantes.','3.1'),
]
EX[4]=[
 mc('Qual política define os aplicativos e usos da rede aceitáveis e as consequências da violação?',
    ['Política de uso aceitável (AUP)','Política de senhas','Política de acesso remoto','Política de manutenção de rede'],
    'A AUP diz o que pode e o que não pode ser feito com a rede da organização.','4.3'),
 mc('O que significa BYOD?',
    ['Uso de aparelhos pessoais dos funcionários no trabalho','Compra de aparelhos pela empresa para uso exclusivo no trabalho','Bloqueio de dispositivos móveis na rede','Backup de dados em dispositivos externos'],
    'BYOD (Bring Your Own Device): o funcionário usa o próprio dispositivo.','4.4'),
 mc('Qual é um risco típico do BYOD?',
    ['Vazamento de dados da empresa a partir de aparelhos pessoais','Menor produtividade garantida','Fim da necessidade de senhas','Aumento do custo de TI com aparelhos novos'],
    'O BYOD traz produtividade e mobilidade, mas aumenta o risco de vazamento de dados.','4.4'),
 mc('Que tipo de política é criada pelo RH e assinada na contratação, com salário, benefícios e férias?',
    ['Política de funcionários','Política de segurança','Política de uso aceitável','Política de tratamento de incidentes'],
    'As políticas de funcionários são criadas e mantidas pelo RH.','4.1'),
]
EX[5]=[
 multi('Indique o estado dos dados em cada situação.',[
    C('Arquivo guardado no disco de um servidor',['Em repouso','Em trânsito','Em processamento'],'Em repouso'),
    C('Mensagem viajando pela internet',['Em repouso','Em trânsito','Em processamento'],'Em trânsito'),
    C('Planilha aberta sendo editada',['Em repouso','Em trânsito','Em processamento'],'Em processamento')],
    'Repouso → armazenados; trânsito → sendo transmitidos; processamento → sendo usados.','5.2'),
 mc('Qual algoritmo simétrico é o recomendado hoje?',
    ['AES','DES','RC4','3DES'],
    'O AES usa bloco de 128 bits e chaves de 128, 192 ou 256 bits. DES, RC4 e 3DES não devem ser usados.','5.3'),
 mc('Para enviar uma mensagem que só Bob possa ler, com qual chave Alice deve criptografá-la?',
    ['Com a chave pública de Bob','Com a chave privada de Bob','Com a própria chave privada','Com a própria chave pública'],
    'Confidencialidade: criptografa com a pública do destinatário; só a privada dele descriptografa.','5.5'),
 mc('O que o Diffie-Hellman permite?',
    ['Que dois computadores gerem o mesmo segredo compartilhado sem enviá-lo pela rede','Que um arquivo seja assinado digitalmente','Que uma senha seja guardada como hash','Que um certificado seja revogado'],
    'O DH cria a chave secreta compartilhada; depois um algoritmo simétrico criptografa os dados.','5.6'),
 mc('Por que, na prática, se usam juntos um algoritmo assimétrico e um simétrico?',
    ['O assimétrico troca a chave com segurança e o simétrico, mais rápido, criptografa o grande volume de dados','O simétrico troca a chave e o assimétrico criptografa os dados','Porque um sozinho não criptografa nada','Para dobrar o tamanho da chave'],
    'Assimétrico → lento, mas sem segredo prévio; simétrico → rápido para grandes volumes.','5.7'),
]
EX[6]=[
 assoc('Associe cada elemento das comunicações seguras ao recurso que o garante.',[
    ('Integridade dos dados','Hash'),
    ('Autenticação de origem','HMAC'),
    ('Confidencialidade','Criptografia'),
    ('Não repúdio','Assinatura digital')],
    'Hash → integridade; HMAC → integridade e origem; criptografia → sigilo; assinatura → não repúdio.','6.1'),
 mc('Qual é uma característica de uma função hash?',
    ['É unidirecional: não é possível recuperar a entrada a partir do hash','O tamanho do hash depende do tamanho da entrada','É reversível com a chave certa','Duas entradas diferentes sempre geram o mesmo hash'],
    'O hash tem tamanho fixo, é irreversível e quase nunca se repete para entradas diferentes.','6.2'),
 mc('Qual algoritmo de hash é legado e inseguro?',
    ['MD5','SHA-256','SHA-3','SHA-512'],
    'O MD5 (128 bits) e o SHA-1 têm falhas conhecidas; prefira SHA-256 ou maior.','6.3'),
 mc('Por que o HMAC resiste ao ataque man-in-the-middle e o hash simples não?',
    ['Porque o HMAC depende de uma chave secreta que o atacante não tem','Porque o HMAC é mais longo','Porque o HMAC criptografa a mensagem inteira','Porque o HMAC usa a chave pública do destinatário'],
    'Sem a chave, o atacante não consegue calcular um HMAC válido para a mensagem alterada.','6.6'),
 mc('O que os sistemas guardam para conferir a senha no login?',
    ['Apenas o hash da senha','A senha em texto claro','A senha criptografada com a chave pública do usuário','A senha dividida em duas partes'],
    'No login, o sistema compara o hash da senha digitada com o hash guardado.','6.7'),
]
EX[7]=[
 mc('O que é criptografado em uma assinatura digital?',
    ['O hash do documento, com a chave privada do autor','O documento inteiro, com a chave pública do destinatário','A chave pública do autor','O certificado da CA'],
    'Por isso a assinatura não dá confidencialidade: o documento continua legível.','7.2'),
 mc('Quem emite e assina os certificados digitais em uma PKI?',
    ['A autoridade de certificação (CA)','A autoridade de registro (RA)','O próprio usuário','O navegador'],
    'A RA confere a identidade e encaminha o pedido; quem emite é sempre uma CA.','7.5'),
 mc('Qual topologia de PKI escala bem e é ideal para grandes organizações?',
    ['Hierárquica','Raiz única','Certificação cruzada','Ponto a ponto'],
    'Na hierárquica, a CA raiz certifica CAs subordinadas que atendem áreas ou domínios.','7.7'),
 mc('Qual padrão define o formato dos certificados digitais?',
    ['X.509 versão 3','PKCS #12','RFC 2527','SHA-2'],
    'O X.509 v3 é o formato usado em HTTPS, VPNs, e-mail seguro e outras aplicações.','7.8'),
 mc('Qual método consulta um servidor, em tempo real, sobre o status de um certificado?',
    ['OCSP','CRL','DSA','IKE'],
    'A CRL é uma lista de certificados revogados consultada periodicamente; o OCSP é a consulta on-line.','7.9'),
]
EX[8]=[
 mc('Qual técnica de mascaramento troca os valores da própria coluna entre os registros?',
    ['Embaralhamento','Substituição','Anulação','Esteganografia'],
    'Exemplo: salários trocados de lugar num banco de testes.','8.1'),
 mc('Qual é a vantagem da esteganografia sobre a criptografia?',
    ['A mensagem secreta não chama atenção','A mensagem fica ilegível sem a chave','Ela dispensa qualquer arquivo de cobertura','Ela é mais rápida que o AES'],
    'Quem vê a imagem não desconfia de que ela carrega algo.','8.2'),
 mc('Na técnica LSB, o que é alterado em cada pixel?',
    ['O último bit de cada byte de cor','O primeiro bit de cada byte de cor','O tamanho da imagem','O formato do arquivo'],
    'A mudança no bit menos significativo é imperceptível ao olho humano.','8.2'),
 mc('Como se chama a descoberta de informações escondidas por esteganografia?',
    ['Esteganoanálise','Criptoanálise','Mascaramento','Ofuscação'],
    'A esteganoanálise procura sinais de que um arquivo carrega uma mensagem oculta.','8.3'),
]
EX[9]=[
 multi('Classifique cada controle de acesso.',[
    C('Cerca e porta trancada',['Físico','Lógico','Administrativo'],'Físico'),
    C('Firewall e criptografia',['Físico','Lógico','Administrativo'],'Lógico'),
    C('Treinamento e verificação de antecedentes',['Físico','Lógico','Administrativo'],'Administrativo')],
    'Físicos → barreiras reais; lógicos → hardware e software; administrativos → políticas e procedimentos.','9.1'),
 assoc('Associe cada serviço do AAA à pergunta que ele responde.',[
    ('Autenticação','Quem é você?'),('Autorização','O que você pode fazer?'),('Contabilidade','O que você fez?')],
    'Autenticação prova a identidade; autorização define permissões; contabilidade registra as ações.','9.2'),
 multi('Indique o fator de autenticação de cada exemplo.',[
    C('PIN',['Algo que você sabe','Algo que você tem','Algo que você é'],'Algo que você sabe'),
    C('Token',['Algo que você sabe','Algo que você tem','Algo que você é'],'Algo que você tem'),
    C('Impressão digital',['Algo que você sabe','Algo que você tem','Algo que você é'],'Algo que você é')],
    'Os três fatores são conhecimento, posse e característica física.','9.4'),
 mc('Por que duas senhas não formam autenticação multifator?',
    ['Porque são do mesmo tipo de fator','Porque senhas não são fatores de autenticação','Porque a MFA exige biometria','Porque duas senhas são mais seguras que a MFA'],
    'A MFA exige fatores de tipos diferentes, como o cartão (tem) e o PIN (sabe) no caixa eletrônico.','9.5'),
]
EX[10]=[
 assoc('Associe cada modelo de controle de acesso a quem decide.',[
    ('DAC','O dono dos dados'),('MAC','Rótulos de segurança e autorização do usuário'),
    ('RBAC','A função ou cargo do usuário'),('ABAC','Atributos do usuário, do recurso e do ambiente')],
    'DAC é o menos restritivo; MAC, o mais rígido; RBAC, o recomendado para grandes organizações.','10.1'),
 mc('Qual princípio diz que cada usuário deve ter só o acesso necessário ao trabalho?',
    ['Privilégio mínimo','Confiança zero','Escalação de privilégios','Diversidade'],
    'O privilégio mínimo reduz o dano possível de uma conta comprometida.','10.2'),
 mc('Qual é o princípio da confiança zero?',
    ['Nunca confie, sempre verifique','Confie em quem está dentro da rede','Bloqueie todos os usuários externos','Verifique só no primeiro acesso'],
    'Na confiança zero, nada é confiável automaticamente, nem dentro da rede.','10.3'),
 mc('O que faz um sistema NAC?',
    ['Aplica as políticas da organização a quem e ao que se conecta à rede','Criptografa o tráfego da rede','Distribui endereços IP','Faz backup dos servidores'],
    'O NAC verifica usuários e dispositivos antes de liberar o acesso à rede.','10.4'),
]
EX[11]=[
 mc('Para que deve ser usada a conta de administrador?',
    ['Apenas para administrar o sistema','Para o uso diário dos recursos','Para usuários temporários','Para programas interagirem com o sistema'],
    'O uso diário deve ser feito com uma conta de usuário comum.','11.1'),
 mc('Qual recurso dispara uma ação quando o usuário entra ou sai de uma área?',
    ['Delimitação geográfica (geofencing)','Geolocalização','Marcação geográfica (geotagging)','SSO'],
    'Exemplo: bloquear o acesso fora do prédio da empresa.','11.2'),
 mc('Ao mover um arquivo dentro do mesmo volume NTFS, o que acontece com as permissões?',
    ['Mantém as permissões originais','Herda as permissões da pasta de destino','Perde todas as permissões','Recebe Controle total'],
    'Mover no mesmo volume mantém; mover para outro volume ou copiar faz herdar novas permissões.','11.4'),
 mc('Qual protocolo envia nome de usuário e senha em texto claro?',
    ['PAP','CHAP','Kerberos','TACACS+'],
    'O PAP é fraco; o CHAP usa desafio e resposta com hash.','11.7'),
 mc('O que o usuário recebe do Kerberos depois de se autenticar?',
    ['Um tíquete de concessão de tíquete (TGT)','Um certificado X.509','Uma chave pública','Um endereço IP'],
    'Com o TGT, o cliente pede acesso aos servidores específicos sem enviar a senha de novo.','11.7'),
]
EX[12]=[
 mc('Quando o AAA local é indicado?',
    ['Em redes pequenas, com poucos roteadores','Em redes grandes, com muitos roteadores','Quando há um servidor RADIUS','Quando a contabilidade precisa ser centralizada'],
    'No AAA local, cada roteador tem a própria lista de usuários, o que não escala.','12.1'),
 multi('Complete a comparação entre TACACS+ e RADIUS.',[
    C('Transporte do TACACS+',['TCP, porta 49','UDP, portas 1812 e 1813'],'TCP, porta 49'),
    C('Transporte do RADIUS',['TCP, porta 49','UDP, portas 1812 e 1813'],'UDP, portas 1812 e 1813'),
    C('Criptografa todo o corpo do pacote',['TACACS+','RADIUS'],'TACACS+'),
    C('É padrão aberto (RFC)',['TACACS+','RADIUS'],'RADIUS')],
    'O RADIUS criptografa só a senha; o TACACS+ separa as três funções do AAA e autoriza comandos.','12.2'),
 mc('Qual tipo de contabilidade do AAA registra os comandos digitados em um nível de privilégio?',
    ['De comandos','De rede','EXEC','Do sistema'],
    'Ela registra cada comando, com data, hora e usuário.','12.3'),
]
EX[13]=[
 mc('Qual erro biométrico é mais grave no controle de acesso?',
    ['Falsa aceitação (tipo II)','Falsa rejeição (tipo I)','Os dois são igualmente graves','Nenhum dos dois'],
    'A falsa aceitação deixa entrar quem não deveria.','13.2'),
 mc('O que indica a CER de um sistema biométrico?',
    ['O ponto em que as taxas de falsa rejeição e de falsa aceitação se igualam; quanto menor, mais preciso','O tempo de leitura da digital','O número de usuários cadastrados','A distância máxima do leitor'],
    'A CER é usada para comparar a precisão de sistemas biométricos.','13.2'),
 mc('Qual tecnologia rastreia ativos que saem da área segura, sem precisar vê-los?',
    ['Etiquetas RFID','CFTV','Guardas','Cercas'],
    'Ela exige leitores instalados nas saídas.','13.3'),
]
EX[14]=[
 mc('Em qual ambiente se confirma que o software funciona com as configurações de segurança antes de ir para produção?',
    ['Preparação (staging)','Desenvolvimento e teste','Produção','Provisionamento'],
    'O staging é idêntico ao ambiente de produção.','14.1'),
 mc('Qual risco têm em comum a reutilização de código e os SDKs de terceiros?',
    ['Uma vulnerabilidade no código reaproveitado passa para o software novo','Eles impedem a validação de entrada','Eles exigem código-fonte aberto','Eles tornam o software mais lento'],
    'O ganho de tempo vem junto com as falhas que o código original já tinha.','14.2'),
 mc('Uma idade digitada precisa estar entre 0 e 120. Que critério de validação de entrada é esse?',
    ['Intervalo','Tamanho','Formato','Consistência'],
    'Intervalo → valor entre um mínimo e um máximo.','14.3'),
 inp('Calcule o dígito verificador do ISBN-10 cujos nove primeiros dígitos são 0 3 0 6 4 0 6 1 5.',['2'],'num',
    'Produtos: 0+27+0+42+24+0+24+3+10 = 130. O múltiplo de 11 seguinte é 132; 132 − 130 = 2.','14.3.1',ph='dígito'),
]
EX[15]=[
 multi('Indique a alternativa segura de cada protocolo.',[
    C('Telnet',['SSH','HTTPS','SNMPv3','DNSSEC'],'SSH'),
    C('HTTP',['SSH','HTTPS','SNMPv3','DNSSEC'],'HTTPS'),
    C('SNMPv1 e v2',['SSH','HTTPS','SNMPv3','DNSSEC'],'SNMPv3'),
    C('DNS sem autenticação',['SSH','HTTPS','SNMPv3','DNSSEC'],'DNSSEC')],
    'Os protocolos inseguros devem ser trocados por versões que criptografam ou autenticam.','15.5'),
 mc('Em uma captura de pacotes de uma sessão SSH, o que o atacante consegue ver?',
    ['Apenas os endereços IP','O usuário e a senha','Todos os comandos digitados','A configuração do roteador'],
    'No Telnet tudo vai em texto claro; no SSH tudo é criptografado.','15.3'),
 inp('Qual é a porta TCP do SSH?',['22'],'num','Telnet → TCP 23; SSH → TCP 22.','15.3',ph='porta'),
 mc('Qual é a proteção indicada contra servidores de tempo falsos?',
    ['Autenticação NTP','Desativar o DHCP','Usar Telnet','Bloquear o ICMP'],
    'A hora correta é essencial para os logs e para validar certificados.','15.2'),
]
EX[16]=[
 mc('Qual é a diferença entre LAN e VLAN?',
    ['A LAN se baseia em conexões físicas; a VLAN, em conexões lógicas','A VLAN é sempre maior que a LAN','A LAN é sem fio; a VLAN é cabeada','Não há diferença'],
    'A VLAN agrupa dispositivos de forma lógica, independentemente de onde estão ligados.','16.1'),
 mc('O que fica normalmente na DMZ?',
    ['Os servidores que atendem o público, como o servidor web','Os computadores do RH','O banco de dados interno de salários','Os switches de acesso'],
    'A DMZ separa os servidores públicos da rede interna.','16.2'),
 multi('Classifique o nível de confiança de cada zona.',[
    C('LAN privada',['Alta','Médio-alta','Médio-baixa','Baixa'],'Alta'),
    C('Extranet',['Alta','Médio-alta','Médio-baixa','Baixa'],'Médio-alta'),
    C('DMZ',['Alta','Médio-alta','Médio-baixa','Baixa'],'Médio-baixa'),
    C('Internet',['Alta','Médio-alta','Médio-baixa','Baixa'],'Baixa')],
    'Quanto maior o risco da zona, menor a confiança.','16.2'),
]
EX[17]=[
 multi('Coloque os padrões de segurança Wi-Fi em ordem de evolução.',[
    C('1º',['WEP','WPA','WPA2','WPA3'],'WEP'),C('2º',['WEP','WPA','WPA2','WPA3'],'WPA'),
    C('3º',['WEP','WPA','WPA2','WPA3'],'WPA2'),C('4º',['WEP','WPA','WPA2','WPA3'],'WPA3')],
    'WEP → WPA → WPA2 → WPA3; o WEP é fraco e não deve ser usado.','17.1'),
 mc('Por que o WPS deve ser desativado?',
    ['Porque o PIN pode ser descoberto por força bruta','Porque deixa a rede mais lenta','Porque exige certificado no cliente','Porque só funciona com WEP'],
    'O WPS facilita a conexão, mas tem uma vulnerabilidade grave.','17.1'),
 mc('Qual método EAP é o mais seguro e o mais difícil de implantar?',
    ['EAP-TLS','PEAP','EAP-TTLS','EAP-FAST'],
    'O EAP-TLS exige certificado no cliente e no servidor.','17.2'),
 mc('Qual técnica dá acesso administrativo total em um Android, ignorando sua arquitetura de segurança?',
    ['Root','Jailbreak','Sideloading','MDM'],
    'Jailbreak → Apple; root → Android; sideloading → instalar fora da loja aprovada.','17.6'),
]
EX[18]=[
 inp('Quantos minutos de inatividade por ano permite a disponibilidade de 99,999% (cinco noves)? Use duas casas decimais.',['5,26','5.26'],'num',
    '525.600 minutos × 0,00001 = 5,256 ≈ 5,26 minutos.','18.2.1',ph='minutos'),
 inp('Quantos minutos de inatividade por ano permite a disponibilidade de 99,9%?',['525,6','525.6'],'num',
    '525.600 × 0,001 = 525,6 minutos (cerca de 8 horas e 46 minutos).','18.2.1',ph='minutos'),
 mc('Qual tipo de RAID não tem redundância?',
    ['RAID 0','RAID 1','RAID 5','Nenhum'],
    'O RAID 0 só distribui os dados; se um disco falhar, os dados se perdem.','18.4'),
 mc('Por que o STP bloqueia caminhos redundantes entre switches?',
    ['Para evitar loops na rede','Para economizar energia','Para aumentar a largura de banda','Para criptografar o tráfego'],
    'Se o caminho ativo falhar, o STP libera o caminho bloqueado.','18.5'),
 mc('O que os protocolos HSRP, VRRP e GLBP oferecem?',
    ['Redundância do gateway padrão, com um IP virtual','Criptografia entre roteadores','Distribuição de endereços IP','Autenticação de usuários'],
    'Se o roteador ativo falhar, outro assume o IP virtual do primeiro salto.','18.6'),
]
EX[19]=[
 mc('Qual é a principal proteção para os sistemas SCADA?',
    ['Separar a rede SCADA da rede local da empresa','Conectá-los diretamente à internet','Usar o WEP nas comunicações','Desativar os logs'],
    'Os sistemas SCADA foram projetados sem conexão com a rede corporativa e a internet.','19.1'),
 mc('Qual medida é essencial em dispositivos IoT?',
    ['Trocar as credenciais padrão de administrador','Manter as senhas de fábrica para facilitar o suporte','Desativar as atualizações de firmware','Expô-los no Shodan'],
    'As credenciais padrão são publicamente conhecidas.','19.2'),
 mc('Como funciona um ataque de tempo contra sistemas embarcados?',
    ['O atacante mede quanto tempo o sistema leva para responder a entradas diferentes','O atacante altera o relógio do NTP','O atacante desliga o sistema em horários de pico','O atacante usa um malware programado'],
    'É um ataque de canal lateral: explora informações que vazam do funcionamento físico.','19.3'),
 mc('Qual é a função de um honeypot?',
    ['Atrair o atacante para um sistema-isca e revelar como ele age','Proteger diretamente os servidores reais','Criptografar os arquivos','Bloquear todo o tráfego externo'],
    'Ele desvia o atacante dos recursos reais.','19.6'),
]
EX[20]=[
 mc('Por qual informação uma ACL padrão filtra os pacotes?',
    ['Apenas o endereço IPv4 de origem','Origem, destino e portas','Apenas o endereço de destino','O endereço MAC'],
    'A ACL estendida filtra origem, destino, protocolo e portas.','20.2'),
 multi('Indique o tipo de ACL pela faixa de números.',[
    C('1 a 99',['Padrão','Estendida'],'Padrão'),C('100 a 199',['Padrão','Estendida'],'Estendida'),
    C('1300 a 1999',['Padrão','Estendida'],'Padrão'),C('2000 a 2699',['Padrão','Estendida'],'Estendida')],
    'Padrão → 1–99 e 1300–1999; estendida → 100–199 e 2000–2699.','20.2'),
 mc('O que acontece com um pacote que não corresponde a nenhuma ACE?',
    ['É descartado pela negação implícita','É permitido','Volta para o remetente com um aviso','É encaminhado para o servidor de logs'],
    'Toda ACL termina com um deny oculto; por isso precisa de pelo menos um permit.','20.3'),
 inp('Qual é a máscara curinga da rede 192.168.50.0/24?',['0.0.0.255'],'ip','255.255.255.255 − 255.255.255.0 = 0.0.0.255.','20.5',ph='x.x.x.x'),
 inp('Qual é a máscara curinga da rede 172.16.8.64/26?',['0.0.0.63'],'ip','/26 = 255.255.255.192; 255 − 192 = 63.','20.5',ph='x.x.x.x'),
 inp('Qual máscara curinga reúne as redes 10.1.4.0/24 a 10.1.7.0/24 em uma entrada?',['0.0.3.255'],'ip','As quatro redes formam 10.1.4.0/22 (255.255.252.0); a curinga é 0.0.3.255.','20.5',ph='x.x.x.x'),
 multi('Informe o primeiro e o último endereço que correspondem a 192.168.5.16 0.0.0.15.',[
    F('Primeiro','192.168.5.16','ip',ph='x.x.x.x'),F('Último','192.168.5.31','ip',ph='x.x.x.x')],
    '16 = 0001 0000 e 15 = 0000 1111: os 4 primeiros bits são verificados, de 0001 0000 (16) a 0001 1111 (31).','20.5'),
 mc('A que equivale a palavra-chave host em uma ACL?',
    ['À máscara curinga 0.0.0.0','À máscara curinga 255.255.255.255','A qualquer endereço','À máscara de sub-rede /24'],
    'host → um único endereço; any → qualquer endereço.','20.6'),
]
EX[21]=[
 inp('Qual comando aplica a ACL 110 na entrada de uma interface?',['ip access-group 110 in'],'cmd','ip access-group {número | nome} {in | out}.','21.5',ph='comando'),
 mc('Onde deve ser aplicada uma ACL estendida?',
    ['O mais perto possível da origem','O mais perto possível do destino','Sempre na interface de saída para a internet','Somente nas linhas VTY'],
    'Assim o tráfego indesejado não atravessa a rede à toa. A ACL padrão fica perto do destino.','21.7'),
 mc('Qual é o efeito da palavra-chave established?',
    ['Permite só os segmentos TCP com ACK ou RST, ou seja, as respostas de conexões existentes','Permite qualquer conexão TCP iniciada de fora','Bloqueia todo o tráfego UDP','Registra cada pacote no log'],
    'Conexões TCP iniciadas de fora são negadas.','21.4'),
 mc('Qual comando aplica uma ACL às linhas VTY?',
    ['access-class','ip access-group','ip traffic-filter','zone-member security'],
    'Nas linhas VTY: line vty 0 4 → access-class NOME in.','21.5'),
 mc('Ao corrigir uma ACL pelo editor de texto, o que precisa ser feito antes de colar a versão nova?',
    ['Apagar a ACL antiga no roteador','Reiniciar o roteador','Desativar a interface','Nada, a nova substitui a antiga'],
    'Se a nova for colada por cima, as linhas apenas se somam às antigas.','21.6'),
 mc('Por que o SSH e o HTTPS precisam ser escritos pelo número da porta em uma ACL?',
    ['Porque não têm nome na lista de portas do IOS','Porque usam UDP','Porque são protocolos de camada 3','Porque o IOS não permite filtrá-los'],
    'SSH → 22; HTTPS → 443.','21.3'),
]
EX[22]=[
 mc('Qual destes endereços de origem a interface voltada para a internet nunca deve aceitar?',
    ['10.0.0.5','8.8.8.8','200.160.2.3','1.1.1.1'],
    'Endereços privados, loopback, APIPA, multicast, broadcast e 0.0.0.0 não chegam legitimamente da internet.','22.1'),
 multi('Indique se cada mensagem ICMP deve ser permitida entrando na rede.',[
    C('echo-reply',['Permitir','Bloquear'],'Permitir'),C('unreachable',['Permitir','Bloquear'],'Permitir'),
    C('echo',['Permitir','Bloquear'],'Bloquear'),C('redirect',['Permitir','Bloquear'],'Bloquear')],
    'Echo serve para reconhecimento e inundação; redirect altera a tabela de roteamento dos hosts.','22.3'),
 mc('Qual é a forma mais eficaz de proteger o SNMP quando ele não é necessário?',
    ['Desativá-lo com no snmp-server','Filtrá-lo com uma ACL padrão','Trocar para SNMPv1','Mudar a porta'],
    'Pacotes com origem falsificada ainda podem passar por uma ACL.','22.4'),
 mc('Qual é uma diferença das ACLs IPv6 em relação às IPv4?',
    ['Não existe ACL IPv6 padrão: todas são nomeadas','Elas só filtram o endereço de origem','São aplicadas com ip access-group','Terminam permitindo tudo'],
    'São aplicadas com ipv6 traffic-filter e terminam permitindo nd-na e nd-ns e negando o resto.','22.6'),
 mc('O que acontece se um deny ipv6 any any explícito for escrito sem antes permitir nd-na e nd-ns?',
    ['O NDP para de funcionar','Nada, o efeito é o mesmo do implícito','O IPv4 também é bloqueado','A ACL é recusada pelo roteador'],
    'Sem as mensagens de vizinho, os dispositivos deixam de descobrir uns aos outros.','22.6'),
]
EX[23]=[
 assoc('Associe cada tipo de firewall às camadas que analisa.',[
    ('Filtragem de pacotes','3 e 4'),('Com estado','3, 4 e 5'),('Gateway de aplicação','3, 4, 5 e 7')],
    'O NGFW vai até a camada 7 e acrescenta controle de aplicativos e prevenção de intrusão.','23.2'),
 mc('Qual é uma limitação do firewall de filtragem de pacotes?',
    ['Examina cada pacote isoladamente, sem saber se ele faz parte de uma conexão','Tem alto impacto no desempenho','Não está disponível em roteadores','É muito difícil de implantar'],
    'Ele não guarda estado e é suscetível à falsificação de IP.','23.3'),
 mc('Qual é uma limitação do firewall com estado?',
    ['Não inspeciona a camada de aplicação','Não acompanha conexões','Não defende contra falsificação','Tem desempenho pior que o proxy'],
    'Ele não enxerga, por exemplo, o conteúdo de uma página HTTP.','23.4'),
 multi('Como um firewall com DMZ trata cada tráfego?',[
    C('Pública → privada',['Bloqueado','Permitido seletivamente','Inspecionado, com pouca restrição'],'Bloqueado'),
    C('Pública → DMZ',['Bloqueado','Permitido seletivamente','Inspecionado, com pouca restrição'],'Permitido seletivamente'),
    C('Privada → pública',['Bloqueado','Permitido seletivamente','Inspecionado, com pouca restrição'],'Inspecionado, com pouca restrição')],
    'DMZ → privada também é geralmente bloqueado.','23.5'),
 mc('O que o firewall não faz?',
    ['Impedir invasões entre hosts da mesma rede ou zona','Filtrar o tráfego entre redes diferentes','Registrar logs','Aplicar a política de acesso'],
    'Ele também não substitui backup nem usuários bem informados.','23.7'),
]
EX[24]=[
 mc('No ZPF, o que acontece com o tráfego entre interfaces da mesma zona?',
    ['Passa livremente, sem política','É sempre inspecionado','É descartado','Depende de uma ACL'],
    'Entre zonas diferentes, o tráfego é bloqueado, a menos que uma política o permita.','24.1'),
 assoc('Associe cada ação do ZPF ao seu efeito.',[
    ('Inspect','Inspeção com estado, permitindo as respostas'),('Pass','Permite sem estado e em um único sentido'),('Drop','Descarta em silêncio')],
    'Drop é a ação padrão; para a maioria das aplicações, a recomendada é Inspect.','24.4'),
 multi('Coloque as etapas de configuração do ZPF em ordem.',[
    C('1ª',['Criar as zonas','Definir o class-map','Definir o policy-map','Criar o zone-pair','Atribuir as interfaces'],'Criar as zonas'),
    C('2ª',['Criar as zonas','Definir o class-map','Definir o policy-map','Criar o zone-pair','Atribuir as interfaces'],'Definir o class-map'),
    C('3ª',['Criar as zonas','Definir o class-map','Definir o policy-map','Criar o zone-pair','Atribuir as interfaces'],'Definir o policy-map'),
    C('4ª',['Criar as zonas','Definir o class-map','Definir o policy-map','Criar o zone-pair','Atribuir as interfaces'],'Criar o zone-pair'),
    C('5ª',['Criar as zonas','Definir o class-map','Definir o policy-map','Criar o zone-pair','Atribuir as interfaces'],'Atribuir as interfaces')],
    'O class-map precisa existir antes do policy-map, e o policy-map antes do zone-pair.','24.6'),
 mc('O que acontece com o tráfego entre uma interface em zona e outra que não está em zona?',
    ['É descartado','Passa livremente','É inspecionado','Segue a ACL da interface'],
    'O tráfego nunca flui entre uma interface com zona e outra sem zona.','24.5'),
 mc('Qual é a zona que representa o próprio roteador?',
    ['Zona self','Zona PRIVATE','Zona DMZ','Zona default'],
    'Por padrão, o tráfego de e para o roteador passa, a menos que haja par de zonas com política.','24.1'),
]
EX[25]=[
 mc('Qual hypervisor roda diretamente sobre o hardware?',
    ['Tipo 1 (bare metal)','Tipo 2 (hospedado)','Contêiner','VDI'],
    'Exemplos de tipo 1: VMware ESXi e Hyper-V; de tipo 2: VirtualBox e VMware Workstation.','25.1'),
 mc('Qual é a diferença entre máquina virtual e contêiner?',
    ['O contêiner leva só o aplicativo e as dependências e compartilha o núcleo do host','O contêiner tem sistema operacional completo','A VM compartilha o núcleo do host','Não há diferença'],
    'Por isso o contêiner é mais leve.','25.2'),
 mc('Como se chama o acúmulo de VMs esquecidas ou subutilizadas?',
    ['Expansão de VMs (VM sprawl)','Fuga de VM (VM escape)','Microssegmentação','Computação de borda'],
    'Na fuga de VM, a VM rompe o isolamento e interage com o host.','25.3'),
 assoc('Associe cada modelo de serviço ao que é entregue.',[
    ('SaaS','Software pronto'),('PaaS','Plataforma para desenvolver e publicar aplicativos'),('IaaS','Recursos de computação virtualizados')],
    'Quanto mais pronto o serviço, mais o provedor gerencia.','25.4'),
 mc('Onde os dados são processados na computação de borda (edge)?',
    ['No próprio dispositivo ou sensor','Em um gateway da rede local','No data center do provedor','Na nuvem pública'],
    'Na computação em neblina (fog), o processamento fica em um equipamento intermediário da rede local.','25.6'),
]
EX[26]=[
 mc('No modelo de responsabilidade compartilhada, qual responsabilidade é sempre do cliente?',
    ['Os dados','A infraestrutura física','O sistema operacional no SaaS','O controle de rede no SaaS'],
    'Em todos os modelos, os dados continuam sendo responsabilidade do cliente.','26.2'),
 mc('No IaaS, quem é responsável pela infraestrutura física?',
    ['O provedor (CSP)','O cliente','Os dois, de forma compartilhada','Ninguém'],
    'No IaaS, o cliente cuida do sistema operacional, das aplicações, da rede e dos dados.','26.2'),
 mc('O que é uma VPC?',
    ['Sub-redes privadas isoladas da internet dentro da nuvem pública','Uma VPN entre dois data centers','Um firewall físico','Um tipo de contêiner'],
    'VPC → nuvem privada virtual.','26.4'),
 mc('Como se chamam os aplicativos e serviços de nuvem que os usuários adotam sem autorização?',
    ['TI invisível (shadow IT)','Microssegmentação','Expansão de VMs','SDN'],
    'Eles criam pontos cegos; a resposta são políticas e conscientização.','26.4'),
 mc('Por que credenciais comprometidas são uma ameaça grave na nuvem pública?',
    ['A conta de serviço tem o maior privilégio, e quem a sequestra controla tudo','Porque a nuvem não usa senhas','Porque o provedor apaga as contas','Porque elas desativam a criptografia'],
    'Também são ameaças graves a configuração incorreta e as APIs inseguras.','26.1'),
]
EX[27]=[
 inp('Qual porta UDP os servidores syslog escutam?',['514'],'num','O NTP usa a porta UDP 123.','27.1',ph='porta'),
 mc('Por que o NTP é essencial para o monitoramento?',
    ['Sem relógios sincronizados, não é possível juntar os rastros de um ataque registrados em equipamentos diferentes','Porque criptografa os logs','Porque substitui o syslog','Porque bloqueia o DNS malicioso'],
    'As mensagens de syslog têm carimbo de data e hora.','27.1'),
 mc('Qual sinal indica retirada de dados pelo DNS?',
    ['Subdomínios muito mais longos que o normal','Consultas a www.google.com','Respostas DNS rápidas','Uso da porta 53'],
    'Consultas a domínios ou subdomínios aleatórios, em grande quantidade, também são suspeitas.','27.2'),
 mc('Qual afirmação sobre o HTTPS está correta?',
    ['Ele protege os dados só no caminho, não o servidor web','Ele impede qualquer ataque ao servidor','Ele dispensa certificados','Ele facilita a inspeção do tráfego'],
    'Para quem monitora, o HTTPS complica a inspeção.','27.3'),
 mc('Por que o PAT dificulta a investigação?',
    ['Todos os dispositivos internos aparecem com o mesmo endereço público','Ele criptografa o tráfego','Ele apaga os logs','Ele muda os endereços MAC'],
    'Fica difícil saber qual dispositivo interno fez cada pedido.','27.5'),
 mc('Por que o P2P de arquivos não deve ser permitido em redes corporativas?',
    ['Contorna o firewall e é uma via de entrada para malware','Porque é mais lento','Porque só funciona com IPv6','Porque exige VPN'],
    'Ele também usa endereços e portas que mudam o tempo todo.','27.7'),
]
EX[28]=[
 assoc('Associe cada tipo de dado de segurança ao que ele registra.',[
    ('Alerta','Violação de uma regra ou assinatura'),('Sessão','Quem conversou com quem, quanto e por quanto tempo'),
    ('Transação','Pedidos e respostas da conversa'),('Captura completa','Todo o conteúdo dos pacotes')],
    'Os dados estatísticos são calculados a partir dos outros.','28'),
 mc('Quais campos formam a 5-tupla que identifica uma sessão?',
    ['IP de origem, IP de destino, porta de origem, porta de destino e protocolo','IP de origem, MAC de origem, porta, protocolo e horário','Usuário, senha, IP, porta e protocolo','IP de destino, DNS, gateway, máscara e porta'],
    'O Zeek registra esses dados no log de conexões.','28.2'),
 mc('Qual tipo de dado exige mais armazenamento?',
    ['Captura completa de pacotes','Dados de sessão','Dados de alerta','Dados estatísticos'],
    'Ela guarda o conteúdo real do que trafegou.','28.4'),
 mc('O que é a linha de base nos dados estatísticos?',
    ['O registro do comportamento normal, comparado ao atual para detectar anomalias','O primeiro pacote de uma sessão','A regra mais antiga do IDS','O endereço do gateway'],
    'Uma diferença estatisticamente significativa gera alarme e investigação.','28.5'),
]
EX[29]=[
 inp('Calcule a prioridade syslog de uma mensagem com facilidade local7 (23) e gravidade 6.',['190'],'num','23 × 8 + 6 = 190.','29.2.1',ph='número'),
 multi('Uma mensagem syslog começa com <165>. Informe a facilidade e a gravidade.',[
    F('Facilidade','20','num',ph='número'),F('Gravidade','5','num',ph='número')],
    '165 ÷ 8 = 20, resto 5: facilidade 20 (local4), gravidade 5 (Notificação).','29.2.1'),
 mc('Na escala de gravidade do syslog, qual valor é o mais grave?',
    ['0 (Emergência)','7 (Depuração)','5 (Notificação)','3 (Erro)'],
    'Quanto menor o número, mais grave o evento.','29.2'),
 mc('Um processo lsass.exe rodando fora da pasta System32 indica o quê?',
    ['Possível malware','Funcionamento normal','Atualização do Windows','Erro de disco'],
    'Nomes disfarçados, como 1sass.exe, também são suspeitos.','29.1'),
 mc('O que o NetFlow registra?',
    ['Informações sobre os fluxos de tráfego, sem o conteúdo','O conteúdo completo dos pacotes','As senhas dos usuários','Apenas as mensagens de erro'],
    'Um fluxo é o conjunto de pacotes em um único sentido com os mesmos atributos.','29.4'),
 assoc('Associe cada solução à sua função principal.',[
    ('SIEM','Reúne, normaliza e correlaciona os eventos'),('SOAR','Automatiza a resposta a incidentes')],
    'SIEM → reúne e correlaciona; SOAR → responde.','29.6'),
]
EX[30]=[
 multi('Classifique cada situação.',[
    C('Houve alerta e o ataque foi confirmado',['Verdadeiro positivo','Falso positivo','Verdadeiro negativo','Falso negativo'],'Verdadeiro positivo'),
    C('Houve alerta por uma varredura autorizada',['Verdadeiro positivo','Falso positivo','Verdadeiro negativo','Falso negativo'],'Falso positivo'),
    C('Tráfego normal, sem alerta',['Verdadeiro positivo','Falso positivo','Verdadeiro negativo','Falso negativo'],'Verdadeiro negativo'),
    C('Ataque sem nenhum alerta',['Verdadeiro positivo','Falso positivo','Verdadeiro negativo','Falso negativo'],'Falso negativo')],
    'Positivo/negativo → houve alerta ou não; verdadeiro/falso → o alerta estava certo ou não.','30.4'),
 mc('Qual caso de classificação de alertas é o mais perigoso?',
    ['Falso negativo','Falso positivo','Verdadeiro positivo','Verdadeiro negativo'],
    'O ataque acontece sem ser visto e pode continuar por muito tempo.','30.4'),
 mc('Qual ferramenta é o ponto de partida da investigação no Security Onion?',
    ['Sguil','Wireshark','Snort','PulledPork'],
    'Do Sguil o analista pivota para o Kibana, o Wireshark e o Zeek.','30.1'),
 mc('Na regra do Snort, o que identifica a regra de forma única?',
    ['sid','msg','rev','classtype'],
    'rev é o número da revisão; msg é o texto exibido no alerta.','30.3'),
 mc('O que é a análise de segurança retrospectiva (RSA)?',
    ['Aplicar regras e informações novas aos dados guardados','Analisar só alertas em tempo real','Apagar logs antigos','Reiniciar o IDS'],
    'Ela descobre falsos negativos depois do fato.','30.4'),
 mc('Qual análise usa estatística para estimar os caminhos mais prováveis de um ataque?',
    ['Probabilística','Determinística','Retrospectiva','Estática'],
    'A determinística parte das etapas conhecidas e descreve o pior caso.','30.5'),
]
