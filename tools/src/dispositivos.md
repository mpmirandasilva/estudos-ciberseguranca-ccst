# Dispositivos de Rede e Configuração Inicial

Oct 29, 2026 · @Maria Paula

## 1. Redes Confiáveis

As redes atuais são **convergentes**: transportam dados, voz e vídeo ao mesmo tempo.

Como muitas pessoas dependem delas para trabalhar e estudar, elas precisam ser **confiáveis**, o que vai além de estar conectado à Internet.

### 1.1 Arquitetura de Rede

A **arquitetura de rede** é o conjunto de tecnologias que sustentam a infraestrutura física, os serviços e as regras (protocolos) que movimentam os dados na rede.

Para atender às expectativas dos usuários, a arquitetura de uma rede deve garantir quatro características básicas:

- tolerância a falhas;
- escalabilidade;
- qualidade de serviço (QoS);
- segurança.

### 1.2 Tolerância a Falhas

Uma **rede tolerante a falhas (fault-tolerant network)** **continua funcionando mesmo quando um ou mais componentes falham**, limitando os dispositivos afetados e permitindo recuperação rápida.

Para isso, ela utiliza vários caminhos entre a origem e o destino. Se um caminho falhar, as mensagens são enviadas imediatamente por outro.

A existência de vários caminhos para um mesmo destino é chamada de **redundância**.

#### 1.2.1 Comutação de Pacotes

Uma das formas de oferecer redundância é a **comutação de pacotes**, que divide uma mensagem em vários blocos menores, chamados **pacotes**.

Cada pacote carrega os endereços de origem e de destino, e os roteadores escolhem o melhor caminho para cada um.

Dessa forma:

- pacotes de uma mesma mensagem podem seguir caminhos diferentes até o destino;
- se um enlace falhar, o roteador altera a rota automaticamente;
- o usuário não percebe a mudança de caminho.

### 1.3 Escalabilidade

Uma rede **escalável** se expande rapidamente para atender novos usuários e aplicações, sem prejudicar o desempenho dos serviços já utilizados.

Isso é possível porque os projetistas **seguem padrões e protocolos aceitos**.

Exemplo: uma nova rede de um departamento pode ser conectada à rede existente de uma empresa sem alterar o funcionamento das demais.

### 1.4 Qualidade de Serviço (QoS)

A **QoS (Quality of Service – Qualidade de Serviço)** é o mecanismo que gerencia o congestionamento e garante a entrega confiável do conteúdo a todos os usuários.

#### 1.4.1 Largura de Banda e Congestionamento

A **largura de banda** é a quantidade de bits que pode ser transmitida em um segundo, medida em **bits por segundo (bps)**.

O **congestionamento** acontece quando a demanda por largura de banda é maior que a quantidade disponível. Nesse caso, os dispositivos guardam os pacotes temporariamente em uma área de memória chamada **buffer**, até que haja recursos para transmiti-los.

#### 1.4.2 Priorização do Tráfego

Com uma política de QoS configurada, o roteador prioriza o tráfego sensível ao tempo, como a voz, quando a rede fica congestionada.

Exemplo: entre uma página Web e uma ligação, o roteador prioriza a ligação, porque um atraso na voz corta a conversa.

É importante observar que a QoS considera o **tipo** de tráfego, e não o seu conteúdo.

**Importante:** a QoS **não aumenta a largura de banda**; ela apenas decide **quem passa primeiro** quando a rede está congestionada.

### 1.5 Segurança de Rede

Os administradores precisam tratar dois tipos de segurança:

- **segurança da infraestrutura de rede**: proteger fisicamente os equipamentos (**roteadores, switches, servidores, cabos e pontos de acesso**) e impedir o acesso não autorizado ao software de gerenciamento instalado neles;
- **segurança da informação**: proteger os dados transmitidos pela rede e os dados armazenados nos dispositivos conectados.

#### 1.5.1 Requisitos da Segurança da Informação

A segurança da informação se baseia em três requisitos principais:

- **confidencialidade**: apenas os destinatários autorizados podem acessar e ler os dados;
- **integridade**: os dados não são alterados durante a transmissão, da origem ao destino;
- **disponibilidade**: os usuários autorizados têm acesso confiável e no momento certo aos serviços e dados.

Esses três requisitos são conhecidos como **Tríade CIA (Confidentiality, Integrity and Availability)**.

#### 1.5.2 Firewall

Um dos principais recursos de segurança é o **firewall**, que **monitora e controla o tráfego, permitindo apenas as comunicações autorizadas**. Funciona como um "porteiro digital".

- **Firewall pessoal (software)** → protege um único dispositivo;
- **Firewall de rede** → protege toda a rede de uma organização e fica na **borda da rede**, entre a rede interna e a Internet.

### 1.6 Resumo das Características de uma Rede Confiável

| Característica | O que garante | Como é obtida |
| --- | --- | --- |
| Tolerância a falhas | Funcionamento mesmo quando algo falha | Redundância e comutação de pacotes |
| Escalabilidade | Crescimento sem perda de desempenho | Uso de padrões e protocolos aceitos |
| QoS | Entrega adequada do tráfego sensível ao tempo | Priorização por tipo de tráfego |
| Segurança | Proteção da infraestrutura e da informação | Confidencialidade, integridade e disponibilidade |

## 2. Design de Rede Hierárquico

O **design hierárquico** é um modelo que divide uma rede grande em redes menores e mais fáceis de gerenciar, organizadas em camadas com funções diferentes.

Para entender por que essa divisão é necessária, é preciso conhecer primeiro os dois endereços que todo dispositivo usa para se comunicar.

### 2.1 Endereços Físicos e Lógicos

Todo dispositivo conectado à rede, chamado de **host**, tem dois tipos de endereço.

#### 2.1.1 Endereço Físico (MAC)

O **endereço MAC (Media Access Control)** é o endereço gravado na placa de rede (NIC – Network Interface Card) do dispositivo.

É o **endereço físico**: **não muda**, onde quer que o host esteja, como o nome de uma pessoa.

O endereço MAC identifica o dispositivo, mas não indica onde ele está localizado na rede.

#### 2.1.2 Endereço Lógico (IP)

O **endereço IP (Internet Protocol)** é atribuído ao host **de acordo com a rede** em que ele está conectado.

É o **endereço lógico**: **muda quando o host troca de rede**, como o endereço residencial de uma pessoa.

O endereço IP é formado por duas partes:

- **porção de rede**: identifica a rede; é igual para todos os hosts da mesma rede local;
- **porção de host**: identifica cada dispositivo dentro da rede; é diferente para cada host.

Os dois endereços são necessários para a comunicação, da mesma forma que o nome e o endereço são necessários para entregar uma carta.

**Importante:** o endereço MAC diz **quem** é o dispositivo; o endereço IP diz **onde** ele está.

| Característica | Endereço MAC | Endereço IP |
| --- | --- | --- |
| Tipo | Físico | Lógico |
| Onde está | Gravado na placa de rede | Configurado no dispositivo |
| Muda se o host trocar de rede? | Não | Sim |
| O que informa | Quem é o dispositivo | Onde o dispositivo está |
| Comparação | Nome da pessoa | Endereço residencial |

### 2.2 Por que Dividir as Redes

Entregar uma carta só com o nome da pessoa, sem endereço, seria quase impossível. O mesmo vale para uma rede que usasse apenas endereços MAC.

Além disso, a Ethernet usa muitos **broadcasts** (mensagens enviadas **a todos os hosts da rede**), que consomem largura de banda.

Por esses dois motivos, redes Ethernet grandes, com muitos hosts, não são eficientes:

- seria difícil localizar um host identificado apenas pelo endereço MAC;
- o volume de broadcasts sobrecarregaria a rede.

A solução é dividir a rede em redes menores, usando um modelo de design hierárquico.

### 2.3 Vantagens do Design Hierárquico

As redes hierárquicas crescem com facilidade e oferecem as seguintes vantagens:

- **escalabilidade**: novas partes podem ser adicionadas sem reorganizar toda a rede;
- **redundância**: as camadas superiores podem ter conexões duplicadas, evitando interrupções;
- **desempenho**: o tráfego local permanece local, e os broadcasts ficam restritos a cada rede menor;
- **segurança**: o acesso entre as redes pode ser controlado nos pontos de conexão;
- **facilidade de gerenciamento e manutenção**: cada camada tem uma função definida, o que facilita a configuração e a solução de problemas.

### 2.4 Camadas do Modelo Hierárquico

O modelo hierárquico organiza a rede em três camadas: acesso, distribuição e núcleo.

![Modelo hierárquico: conexões redundantes entre as camadas superiores; os usuários se conectam na camada de acesso](img/dispositivos/hierarquico.png){width=6in}


#### 2.4.1 Camada de Acesso

A camada de acesso fornece o ponto de conexão à rede para os dispositivos dos usuários.

É nela que se conectam **computadores, telefones IP, servidores, impressoras** e os **pontos de acesso sem fio**.

Os dispositivos típicos dessa camada são switches e pontos de acesso sem fio. Exemplo: switch Cisco 2960-XR.

Normalmente, todos os hosts de uma mesma camada de acesso têm a mesma porção de rede no endereço IP. Com base nessa porção:

- **destino na mesma rede** → a mensagem **permanece local**;
- **destino em outra rede** → a mensagem é enviada para a **camada de distribuição**.

#### 2.4.2 Camada de Distribuição

A camada de distribuição conecta as redes separadas e controla o fluxo de informações entre elas.

Ela controla o tipo e a quantidade de tráfego que passa da camada de acesso para a camada de núcleo.

Seus dispositivos são **switches mais potentes e roteadores**. Exemplo: switches Cisco C9300.

#### 2.4.3 Camada de Núcleo

A camada de núcleo é o backbone de alta velocidade da rede, com conexões redundantes.

Ela é responsável por transportar grandes volumes de dados rapidamente entre as várias redes.

Seus dispositivos são roteadores e **switches modulares de alta velocidade**. Exemplo: Cisco Catalyst 9600.

### 2.5 Comparativo das Camadas

| Camada | Função principal | Dispositivos típicos | Exemplo |
| --- | --- | --- | --- |
| Acesso | Conectar os dispositivos dos usuários | Switches e pontos de acesso | Cisco 2960-XR |
| Distribuição | Conectar as redes e controlar o tráfego entre elas | Switches potentes e roteadores | Cisco C9300 |
| Núcleo | Transportar grandes volumes de dados rapidamente | Roteadores e switches de alta velocidade | Cisco Catalyst 9600 |

## 3. Nuvem e Virtualização

Quando se fala em "nuvem", normalmente se fala de três elementos:

- data centers;
- serviços de computação em nuvem;
- virtualização.

### 3.1 Data Centers

Um **data center** é uma grande instalação que concentra servidores e fornece grande quantidade de energia, refrigeração e largura de banda.

Poucas empresas mantêm data center próprio; a maioria aluga serviços de provedores como **Amazon Web Services (AWS)**, **Microsoft Azure** e a própria **Cisco**.

### 3.2 Serviços de Nuvem

Os provedores oferecem três tipos principais de serviço, que se diferenciam por quanto do ambiente fica sob responsabilidade do provedor:

- **SaaS (Software as a Service – Software como Serviço)**: o provedor entrega o **software pronto, sob demanda**, normalmente por **assinatura** e acessado pelo navegador. Exemplos: **Microsoft 365** e **Adobe Creative Cloud**;
- **PaaS (Platform as a Service – Plataforma como Serviço)**: o provedor entrega a **plataforma para desenvolvedores criarem aplicações**, com ferramentas, bancos de dados e ambientes de desenvolvimento, sem que o cliente precise gerenciar a infraestrutura;
- **IaaS (Infrastructure as a Service – Infraestrutura como Serviço)**: o provedor entrega **recursos de infraestrutura virtualizados** (servidores, armazenamento e rede), provisionados **conforme a necessidade**, e o cliente instala e gerencia o restante.

| Serviço | O que o provedor entrega | O que o cliente gerencia |
| --- | --- | --- |
| SaaS | O aplicativo completo | Apenas o uso do aplicativo |
| PaaS | A plataforma de desenvolvimento | As aplicações e os dados |
| IaaS | Servidores, armazenamento e rede | Sistemas operacionais, aplicações e dados |

### 3.3 Tipos de Nuvem

De acordo com quem pode utilizá-las, as nuvens são classificadas em quatro modelos.

#### 3.3.1 Nuvem Pública

Os serviços da nuvem pública são disponibilizados para a população em geral, pela Internet.

Podem ser gratuitos ou cobrados por uso. Exemplo: armazenamento de arquivos online.

#### 3.3.2 Nuvem Privada

Os serviços da nuvem privada são destinados a uma organização específica, como um órgão do governo.

Pode ficar na rede da própria organização (custo alto) ou ser gerenciada por uma empresa externa, com acesso restrito.

#### 3.3.3 Nuvem Híbrida

A nuvem híbrida é formada por duas ou mais nuvens (por exemplo, uma parte privada e outra pública) conectadas por uma única arquitetura.

Cada parte continua separada, e os usuários podem ter níveis de acesso diferentes a cada serviço.

#### 3.3.4 Nuvem Comunitária

A nuvem comunitária é criada para uso exclusivo de uma comunidade específica.

Seus recursos são **personalizados para aquela comunidade**. Exemplo: organizações de saúde, que precisam cumprir leis de confidencialidade.

| Tipo | Quem utiliza | Característica principal |
| --- | --- | --- |
| Pública | Qualquer pessoa | Acesso pela Internet, gratuito ou pago por uso |
| Privada | Uma organização | Maior controle, custo mais alto |
| Híbrida | Uma organização, com partes públicas e privadas | Combina duas ou mais nuvens |
| Comunitária | Um grupo com necessidades em comum | Personalizada para a comunidade |

### 3.4 O Problema dos Servidores Dedicados

Antes da virtualização, cada servidor corporativo tinha um sistema operacional instalado em um hardware exclusivo, e toda a memória, o processamento e o disco eram dedicados a um único serviço, como **Web, e-mail, banco de dados (SQL), arquivos, DHCP ou Active Directory**.

Esse modelo trazia três problemas:

- **ponto único de falha**: se um componente do servidor falhasse, o serviço ficava indisponível;
- **subutilização**: os recursos do servidor ficavam ociosos durante longos períodos, esperando a demanda pelo serviço;
- **expansão de servidores (server sprawl)**: com um servidor físico para cada serviço, **aumentam o consumo de espaço, energia e refrigeração**.

### 3.5 Virtualização

**Virtualizar** significa criar uma versão virtual, e não física, de um computador.

Exemplo: executar um computador com Linux dentro de um computador com Windows.

Com ela, **um servidor físico executa vários sistemas operacionais**, cada um em uma **máquina virtual (VM – Virtual Machine)**. Ela é **a base da computação em nuvem**.

**Importante:** nuvem e virtualização não são sinônimos: a virtualização é a tecnologia; a nuvem é o serviço oferecido a partir dela.

#### 3.5.1 Vantagens da Virtualização

A principal vantagem é o menor custo geral, obtido pela **consolidação de servidores** (vários servidores virtuais em poucos servidores físicos):

- menos equipamentos, com menor custo de manutenção;
- menor consumo de energia e de refrigeração;
- menos espaço físico.

Outros benefícios são:

- **prototipagem mais fácil**: laboratórios isolados podem ser criados rapidamente para testes;
- **provisionamento mais rápido**: criar um servidor virtual é muito mais rápido que instalar um físico;
- **maior tempo de atividade**: as plataformas oferecem recursos de tolerância a falhas e redundância;
- **recuperação de desastres aprimorada**: é possível testar e automatizar a troca para um sistema reserva (failover) antes que ocorra um problema;
- **suporte a sistemas legados**: sistemas antigos podem continuar funcionando por mais tempo, até a migração.

### 3.6 Hipervisores

O **hipervisor (hypervisor)** é um programa, firmware ou hardware que cria uma camada de abstração sobre o hardware físico.

Cada VM usa os recursos da máquina física (processador, memória, disco, placas de rede) e executa **um sistema operacional completo e separado**.

Exemplo: com a virtualização, é comum consolidar 100 servidores físicos em máquinas virtuais executadas sobre apenas 10 servidores físicos.

Existem dois tipos de hipervisor.

#### 3.6.1 Hipervisor Tipo 1 (Bare Metal)

O hipervisor Tipo 1 é instalado diretamente no hardware, sem um sistema operacional por baixo. Os sistemas operacionais das VMs são instalados sobre ele.

Por ter acesso direto aos recursos do hardware, é mais eficiente e oferece melhor escalabilidade, desempenho e robustez.

É usado principalmente em **servidores corporativos e data centers**. Exemplos: **VMware ESXi**, **Microsoft Hyper-V**, **Xen** e **KVM**.

#### 3.6.2 Hipervisor Tipo 2 (Hospedado)

O hipervisor Tipo 2 é um software instalado sobre um sistema operacional já existente, como Windows, Linux ou macOS. As VMs são criadas dentro dele.

O computador onde ele roda é o **computador host**. Exemplos: **Oracle VirtualBox** e **VMware Workstation**.

Não precisa de software de console de gerenciamento, mas o host precisa ter **recursos suficientes** para as VMs.

**Observação:** a definição geral de hipervisor vale para os dois tipos; só o **Tipo 1** é instalado diretamente no hardware.

#### 3.6.3 Virtualização de Rede

Além dos servidores, também é possível **virtualizar a comutação (switching) e o roteamento**.

As VMs se conectam por **switches virtuais**, como o **Cisco Nexus 1000V**.

### 3.7 Comparativo dos Hipervisores

| Característica | Tipo 1 (Bare Metal) | Tipo 2 (Hospedado) |
| --- | --- | --- |
| Onde é instalado | Diretamente no hardware | Sobre um sistema operacional |
| Acesso ao hardware | Direto | Por meio do sistema operacional |
| Eficiência | Maior | Menor |
| Uso típico | Servidores corporativos e data centers | Computadores pessoais, estudos e testes |

## 4. Sistemas Numéricos

Os dispositivos trabalham em **binário**; as pessoas, em **decimal**. Por isso, os endereços são escritos em decimal ou hexadecimal.

Por isso, antes de estudar os endereços MAC e IP em detalhe, é necessário dominar três sistemas de numeração:

- **decimal (base 10)**: usa os dígitos de 0 a 9;
- **binário (base 2)**: usa apenas os dígitos 0 e 1;
- **hexadecimal (base 16)**: usa os dígitos de 0 a 9 e as letras de A a F.

| Sistema | Base | Dígitos | Uso em redes |
| --- | --- | --- | --- |
| Decimal | 10 | 0 a 9 | Escrita dos endereços IPv4 pelas pessoas |
| Binário | 2 | 0 e 1 | Forma como os dispositivos armazenam e processam os endereços |
| Hexadecimal | 16 | 0 a 9 e A a F | Escrita dos endereços MAC e IPv6 |

### 4.1 Sistema Binário

O sistema binário usa apenas os dígitos 0 e 1, chamados de **bits**.

#### 4.1.1 Notação Posicional

Na **notação posicional**, o valor de um dígito depende da posição que ele ocupa no número.

No binário, **cada posição vale 2 vezes a posição à sua direita**.

Para um grupo de 8 bits, os valores posicionais são:

| Potência | 2⁷ | 2⁶ | 2⁵ | 2⁴ | 2³ | 2² | 2¹ | 2⁰ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Valor posicional | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

Com 8 bits, é possível representar os valores de 0 a 255.

#### 4.1.2 Conversão de Binário para Decimal

Para converter um número binário em decimal, somam-se os valores posicionais das posições que têm o bit 1.

Exemplo: converter 11000000 para decimal.

1. os bits 1 estão nas posições de valor 128 e 64;
2. 128 + 64 = 192;
3. o resultado é 192.

Exemplo: converter 00001011 para decimal: 8 + 2 + 1 = 11.

#### 4.1.3 Exemplo Resolvido: Endereço Completo em Binário

Converter 11000000.10101000.00000001.01100101 para decimal. **Cada octeto é convertido separadamente.**

| Valor posicional | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 | Soma |
|------------------------|---|---|---|---|---|---|---|---|----------------------|
| 1º octeto: 11000000 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 128 + 64 = **192** |
| 2º octeto: 10101000 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 128 + 32 + 8 = **168** |
| 3º octeto: 00000001 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| 4º octeto: 01100101 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 64 + 32 + 4 + 1 = **101** |

Resultado: **192.168.1.101**.

#### 4.1.4 Conversão de Decimal para Binário

Para converter um número decimal em binário, compara-se o número com cada valor posicional, da esquerda para a direita (de 128 até 1):

1. se o número for igual ou maior que o valor posicional, coloca-se o bit 1 nessa posição e subtrai-se o valor posicional do número;
2. se o número for menor, coloca-se o bit 0;
3. repete-se o processo com o resto, na posição seguinte, até chegar à posição de valor 1.

Exemplo: converter 168 para binário.

| Valor posicional | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Comparação | 168 ≥ 128 → resto 40 | 40 < 64 | 40 ≥ 32 → resto 8 | 8 < 16 | 8 ≥ 8 → resto 0 | 0 | 0 | 0 |
| Bit | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |

O resultado é **10101000**.

Com números pequenos, é possível fazer a soma diretamente, sem subtrações. Exemplo: 10 = 8 + 2, então o binário é 00001010.

#### 4.1.5 Exemplo Resolvido: Endereço Completo em Decimal

Converter 172.217.162.142 para binário, escrevendo a **cadeia de subtrações** de cada octeto:

| Octeto | Subtrações | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|-------|--------------------------|-----|-----|-----|-----|-----|-----|-----|-----|
| 172 | 172 − 128 = 44 − 32 = 12 − 8 = 4 − 4 = 0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| 217 | 217 − 128 = 89 − 64 = 25 − 16 = 9 − 8 = 1 − 1 = 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 |
| 162 | 162 − 128 = 34 − 32 = 2 − 2 = 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| 142 | 142 − 128 = 14 − 8 = 6 − 4 = 2 − 2 = 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 |

Resultado: **10101100.11011001.10100010.10001110**.

### 4.2 Endereços IPv4 em Binário e em Decimal

Um **endereço IPv4** é uma sequência de 32 bits, dividida em quatro grupos de 8 bits, chamados **octetos**. Cada octeto corresponde a 1 byte.

Para facilitar a leitura, ele é escrito em **notação decimal pontilhada**: cada octeto em decimal, separados por pontos.

Exemplo: o endereço 192.168.10.10.

| Representação | 1º octeto | 2º octeto | 3º octeto | 4º octeto |
| --- | --- | --- | --- | --- |
| Decimal | 192 | 168 | 10 | 10 |
| Binário | 11000000 | 10101000 | 00001010 | 00001010 |

**Importante:** o dispositivo armazena o endereço como **uma única sequência de 32 bits**; os octetos servem só para a leitura.

### 4.3 Sistema Hexadecimal

O sistema hexadecimal é de base 16 e usa os dígitos de 0 a 9 e as letras de A a F, em que A vale 10 e F vale 15.

É usado em redes porque **um dígito hexadecimal representa exatamente 4 bits**.

| Decimal | Binário | Hexadecimal |
| --- | --- | --- |
| 0 | 0000 | 0 |
| 1 | 0001 | 1 |
| 2 | 0010 | 2 |
| 3 | 0011 | 3 |
| 4 | 0100 | 4 |
| 5 | 0101 | 5 |
| 6 | 0110 | 6 |
| 7 | 0111 | 7 |
| 8 | 1000 | 8 |
| 9 | 1001 | 9 |
| 10 | 1010 | A |
| 11 | 1011 | B |
| 12 | 1100 | C |
| 13 | 1101 | D |
| 14 | 1110 | E |
| 15 | 1111 | F |

#### 4.3.1 Conversões com Hexadecimal

Como 8 bits formam dois grupos de 4 bits, um byte é escrito com dois dígitos hexadecimais, de 00 a FF.

Para converter entre decimal e hexadecimal, passa-se primeiro pelo binário:

1. converte-se o número para binário;
2. divide-se o binário em grupos de 4 bits;
3. converte-se cada grupo no dígito hexadecimal correspondente.

Exemplo: converter 168 para hexadecimal.

1. 168 = 10101000;
2. grupos: 1010 e 1000;
3. 1010 = A e 1000 = 8, portanto 168 = **A8**.

Quando se escreve **um byte** (por exemplo, em um endereço MAC), usam-se sempre **dois dígitos**, mantendo o zero à esquerda. Exemplo: 00001010 é escrito como **0A**, e não como A.

#### 4.3.2 Outros Métodos de Conversão

No hexadecimal, cada posição vale **16 vezes** a posição à sua direita:

| Potência | 16³ | 16² | 16¹ | 16⁰ |
| --- | --- | --- | --- | --- |
| Valor posicional | 4096 | 256 | 16 | 1 |

**Hexadecimal → decimal (multiplicando por 16):** para dois dígitos, **(primeiro dígito × 16) + (segundo dígito × 1)**.

Exemplo: 2B = (2 × 16) + 11 = 32 + 11 = **43**. Conferindo pelo binário: 2 = 0010 e B = 1011 → 00101011 = 32 + 8 + 2 + 1 = 43.

**Decimal → hexadecimal (dividindo por 16):**

1. divide-se o número por 16;
2. o **resto** é o último dígito hexadecimal;
3. o **quociente** é dividido de novo por 16, até ficar menor que 16;
4. os restos são lidos **de baixo para cima**, lembrando que 10 a 15 correspondem a A a F.

Exemplo: 197 ÷ 16 = 12, com resto 5. Como 12 = C, o resultado é **C5**. Conferindo pelo binário: 197 = 11000101 → 1100 = C e 0101 = 5.

**Hexadecimal → binário:** cada dígito vira **4 bits**, mantendo a ordem. Em um endereço IPv6, converte-se grupo por grupo, completando com zeros à esquerda para que cada grupo tenha 16 bits.

#### 4.3.3 Como Indicar que um Número é Hexadecimal

Para diferenciá-lo do decimal, usa-se o prefixo **0x** (0x73), o sufixo H (73H) ou o índice 16 (73₁₆).

### 4.4 Onde o Hexadecimal é Usado

O hexadecimal é usado para escrever endereços MAC e endereços IPv6.

#### 4.4.1 Endereço MAC

O endereço MAC tem 48 bits. Como cada dígito hexadecimal representa 4 bits, ele é escrito com 12 dígitos hexadecimais.

Exemplo: 00-1A-2B-3C-4D-5E.

#### 4.4.2 Endereço IPv6

O **IPv6** é a versão mais recente do protocolo IP. Seu endereço tem 128 bits, escritos com 32 dígitos hexadecimais.

O formato preferencial é **x:x:x:x:x:x:x:x**, em que cada "x" é um **hexteto**: 16 bits, ou quatro dígitos hexadecimais (termo não oficial).

Exemplo: 2001:0db8:acad:0001:0000:0000:0000:0010.

Os endereços IPv6 não diferenciam letras maiúsculas de minúsculas.

| Endereço | Tamanho | Escrita | Agrupamento |
| --- | --- | --- | --- |
| IPv4 | 32 bits | Decimal pontilhado | 4 octetos de 8 bits |
| MAC | 48 bits | Hexadecimal | 6 bytes (12 dígitos) |
| IPv6 | 128 bits | Hexadecimal | 8 hextetos de 16 bits |

## 5. Ethernet e Comutação

A **Ethernet** é a tecnologia usada por quase todas as redes locais (LANs) cabeadas. Ela define como os dados são formatados e transmitidos pelos cabos.

A comunicação em rede costuma ser explicada pelo **modelo OSI**, que divide o processo em sete camadas. A Ethernet atua nas duas primeiras:

- **camada 1 (física)**: transmite os bits pelo meio físico (cabos de cobre, fibra óptica);
- **camada 2 (enlace de dados)**: organiza os bits em **quadros** e entrega esses quadros entre dispositivos da mesma rede local, usando endereços MAC.

### 5.1 A Padronização da Ethernet

Para que equipamentos de marcas diferentes funcionem juntos, foram criados **padrões**: regras comuns a todos os fabricantes.

Os padrões trazem as seguintes vantagens:

- facilitam o projeto das redes;
- simplificam o desenvolvimento de produtos;
- promovem a concorrência;
- garantem interconexões consistentes;
- facilitam o treinamento;
- oferecem mais opções de fornecedores aos clientes.

A Ethernet se tornou o **padrão de fato** das redes locais, ou seja, o usado na prática.

#### 5.1.1 IEEE e o Padrão 802.3

Os padrões Ethernet são mantidos pelo **IEEE (Institute of Electrical and Electronics Engineers – Instituto de Engenheiros Eletricistas e Eletrônicos)**.

Cada padrão recebe o número do comitê responsável por ele. O comitê da Ethernet é o 802.3.

#### 5.1.2 Evolução e Nomenclatura

Criada em 1973, a Ethernet evoluiu de 10 Mbps para 10 Gbps ou mais.

As velocidades suportadas são: 10 Mbps, 100 Mbps, 1 Gbps, 10 Gbps, 40 Gbps e 100 Gbps.

O nome de cada versão indica suas características. Exemplo: **100BASE-T**.

- **100**: velocidade de 100 Mbps;
- **BASE**: transmissão em banda base;
- **T**: tipo de cabo, no caso, par trançado.

### 5.2 Subcamadas de Enlace de Dados

Na Ethernet, a camada de enlace de dados é dividida em duas subcamadas.

#### 5.2.1 Subcamada LLC

A subcamada **LLC (Logical Link Control – Controle de Enlace Lógico)**, definida pelo IEEE 802.2, faz a comunicação entre o software das camadas superiores e o hardware das camadas inferiores.

Ela **indica no quadro qual protocolo de rede é transportado**, permitindo que IPv4 e IPv6 usem a mesma placa.

#### 5.2.2 Subcamada MAC

A subcamada **MAC (Media Access Control – Controle de Acesso ao Meio)**, definida pelo IEEE 802.3, é implementada no hardware e é responsável por encapsular os dados e controlar o acesso ao meio.

O **encapsulamento** é o processo de colocar os dados dentro de um quadro, acrescentando as informações de controle necessárias à entrega. No caso da Ethernet, ele inclui:

- **estrutura do quadro**: a organização interna dos campos;
- **endereçamento**: os endereços MAC de origem e de destino, para entregar o quadro de uma placa de rede a outra na mesma LAN;
- **detecção de erros**: um campo no final do quadro que permite verificar se ele chegou corrompido.

#### 5.2.3 Acesso ao Meio: Half-duplex e Full-duplex

Nas redes Ethernet antigas, que usavam **hubs**, o meio era compartilhado e funcionava em **half-duplex**, ou seja, os dispositivos enviavam ou recebiam, mas não as duas coisas ao mesmo tempo.

Nesse caso, era usado o método **CSMA/CD (Carrier Sense Multiple Access with Collision Detection – Acesso Múltiplo com Detecção de Portadora e Detecção de Colisão)**, que:

- garante que apenas um dispositivo transmita por vez;
- detecta uma colisão quando dois dispositivos transmitem ao mesmo tempo;
- define um tempo de espera antes da retransmissão.

As redes atuais usam **switches** em **full-duplex**, em que os dispositivos enviam e recebem ao mesmo tempo. Por isso, não precisam do CSMA/CD.

### 5.3 Quadro Ethernet

O **quadro Ethernet** é a unidade de dados transmitida na camada de enlace. Ele leva os dados de uma camada superior, normalmente um pacote IPv4 ou IPv6, entre os dispositivos de uma mesma rede local.

#### 5.3.1 Tamanho do Quadro

- Tamanho mínimo: 64 bytes.
- Tamanho máximo: 1518 bytes.

Esses valores contam do campo Endereço MAC de Destino até o campo FCS; o preâmbulo não entra na conta.

O dispositivo que recebe o quadro descarta os quadros fora desses limites, pois provavelmente são resultado de colisões ou de sinais indesejados:

- quadro com menos de 64 bytes: chamado de **fragmento de colisão** ou **quadro desprezível (runt)**;
- quadro com mais de 1500 bytes de dados: chamado de **quadro jumbo** ou **baby giant**. A maioria dos switches e placas Fast Ethernet e Gigabit Ethernet aceita esse tipo de quadro.

#### 5.3.2 Campos do Quadro

| Campo | Tamanho | Função |
| --- | --- | --- |
| Preâmbulo | 7 bytes | Sincroniza o emissor e o receptor, avisando que um quadro vai chegar |
| SFD (Start Frame Delimiter – Delimitador de Início de Quadro) | 1 byte | Marca o início do quadro |
| Endereço MAC de destino | 6 bytes | Identifica o destinatário; pode ser unicast, broadcast ou multicast |
| Endereço MAC de origem | 6 bytes | Identifica a placa de rede que enviou o quadro |
| Tipo/Comprimento (EtherType) | 2 bytes | Indica o protocolo transportado: 0x800 para IPv4, 0x86DD para IPv6 e 0x806 para ARP |
| Dados | 46 a 1500 bytes | Contém o pacote da camada superior; se for pequeno, recebe bits de preenchimento (pad) até o tamanho mínimo |
| FCS (Frame Check Sequence – Sequência de Verificação de Quadro) | 4 bytes | Detecta erros no quadro |

#### 5.3.3 Detecção de Erros (FCS)

O campo FCS utiliza a **CRC (Cyclic Redundancy Check – Verificação de Redundância Cíclica)**:

1. o emissor calcula um valor a partir do conteúdo do quadro e o coloca no campo FCS;
2. o receptor faz o mesmo cálculo com o quadro recebido;
3. se os valores forem iguais, o quadro chegou sem erros; se forem diferentes, os dados foram alterados e o quadro é descartado.

### 5.4 Endereço MAC Ethernet

O endereço MAC tem 48 bits, escritos com 12 dígitos hexadecimais. Exemplo: 00-60-2F-3A-07-BC.

Ele é usado no quadro Ethernet para entregar os dados de uma placa de rede a outra dentro da mesma LAN.

O endereço MAC é **gravado na placa de rede durante a fabricação** e é dividido em duas partes:

- **OUI (Organizationally Unique Identifier)** → os **3 primeiros bytes**, que identificam o **fabricante**;
- **ID da interface** → os **3 últimos bytes**, que identificam a placa de forma única dentro daquele fabricante.

Assim, placas do mesmo fabricante têm o mesmo OUI, mas os 3 últimos bytes são sempre diferentes.

De acordo com o destino, existem três tipos de endereço MAC: unicast, broadcast e multicast.

#### 5.4.1 MAC Unicast

O endereço MAC **unicast** é o endereço exclusivo de um dispositivo, usado quando um quadro vai de um único emissor para um único destinatário.

O **IP de destino vai no pacote**, e o **MAC de destino vai no quadro** que o transporta: os dois trabalham juntos.

Para descobrir o MAC correspondente a um IP, o host usa um protocolo próprio: o **ARP (Address Resolution Protocol)** no IPv4 e o **ND (Neighbor Discovery)** no IPv6.

**Importante:** o endereço MAC de origem é **sempre unicast**.

#### 5.4.2 MAC Broadcast

O quadro de **broadcast** é recebido e processado por todos os dispositivos da LAN. Suas características são:

- o endereço MAC de destino é FF-FF-FF-FF-FF-FF (48 bits iguais a 1);
- o switch o envia por todas as portas, exceto pela porta em que ele chegou;
- não é encaminhado por roteadores, ou seja, fica restrito à rede local.

O conjunto de dispositivos alcançados por um broadcast é chamado de **domínio de broadcast**.

Quando o quadro transporta um pacote IPv4 de broadcast, o endereço IP de destino também é de broadcast. Exemplo: 192.168.1.255, em que a parte que identifica o host tem todos os bits iguais a 1.

Exemplos de uso:

- o DHCP, serviço que distribui endereços IP automaticamente, usa broadcast Ethernet e IPv4;
- as solicitações ARP são enviadas em broadcast Ethernet, **mesmo sem carregar um pacote IPv4**.

#### 5.4.3 MAC Multicast

O quadro **multicast** é recebido e processado apenas pelos dispositivos que pertencem a um mesmo grupo. Suas características são:

- o endereço MAC de destino começa com 01-00-5E quando transporta IPv4 e com 33-33 quando transporta IPv6;
- há outros endereços multicast reservados para protocolos que não usam IP, como o STP (Spanning Tree Protocol) e o LLDP (Link Layer Discovery Protocol);
- o switch o envia por todas as portas, exceto a de entrada, a menos que esteja configurado para filtrar multicast;
- não é encaminhado por roteadores, a menos que eles estejam configurados para isso.

Os endereços IP multicast ficam nas faixas 224.0.0.0 a 239.255.255.255 no IPv4 e ff00::/8 no IPv6.

**Importante:** como um endereço multicast representa um grupo, ele **só pode ser usado como destino**. A origem é sempre **unicast**.

O multicast é usado por protocolos de roteamento e por alguns aplicativos de vídeo.

#### 5.4.4 Comparativo dos Tipos de Endereço MAC

| Tipo | Quem recebe | Endereço MAC de destino | Passa pelo roteador? |
| --- | --- | --- | --- |
| Unicast | Um único dispositivo | Endereço exclusivo do destinatário | Sim, dentro de um novo quadro |
| Broadcast | Todos os dispositivos da LAN | FF-FF-FF-FF-FF-FF | Não |
| Multicast | Um grupo de dispositivos | 01-00-5E (IPv4) ou 33-33 (IPv6) | Somente se configurado |

### 5.5 Funcionamento do Switch

O **switch** é o dispositivo que conecta os hosts de uma rede local e encaminha cada quadro apenas para a porta do destinatário.

O switch de camada 2 decide **apenas pelos endereços MAC**, sem analisar o conteúdo do quadro.

Isso o diferencia dos antigos **hubs**, que repetiam todos os bits por todas as portas, exceto a de entrada, sobrecarregando a rede.

#### 5.5.1 Tabela de Endereços MAC

Para saber em qual porta está cada dispositivo, o switch mantém a **tabela de endereços MAC**, que relaciona cada endereço MAC à porta em que ele está conectado.

Essa tabela também é chamada de **tabela CAM (Content Addressable Memory – Memória Endereçável por Conteúdo)**. Quando o switch é ligado, ela está vazia.

#### 5.5.2 Aprendizado: Examinar o MAC de Origem

O switch aprende os endereços analisando o MAC de origem de cada quadro que recebe:

1. **MAC de origem fora da tabela** → é adicionado junto com o **número da porta de entrada**;
2. **MAC de origem já na tabela** → o **cronômetro** da entrada é reiniciado;
3. **mesmo MAC em outra porta** → a entrada é atualizada para a **porta mais recente**.

Por padrão, a maioria dos switches mantém cada entrada por 5 minutos sem uso.

#### 5.5.3 Encaminhamento: Procurar o MAC de Destino

Em seguida, o switch procura o MAC de destino na tabela:

- **MAC de destino conhecido** → o quadro é enviado **somente pela porta correspondente**. Esse comportamento é chamado de **filtragem**;
- **MAC de destino desconhecido** → o quadro é enviado por **todas as portas, exceto a de entrada**. Esse caso é chamado de **unicast desconhecido**;
- **broadcast ou multicast** → também é enviado por todas as portas, exceto a de entrada.

#### 5.5.4 Exemplo do Processo

Um switch de 4 portas acaba de ser ligado. O PC-A está na porta 1, e o PC-D está na porta 4.

1. PC-A envia um quadro para PC-D: o switch registra o MAC do PC-A na porta 1. Como ainda não conhece o PC-D, envia o quadro para todas as portas, exceto a 1;
2. PC-D responde ao PC-A: o switch registra o MAC do PC-D na porta 4. Como já conhece o PC-A, envia o quadro apenas pela porta 1;
3. PC-A envia outro quadro para PC-D: o switch reinicia o cronômetro da entrada do PC-A e, como já conhece o PC-D, envia o quadro apenas pela porta 4.

Com o tempo, a tabela se completa e o switch passa a **filtrar** quase todos os quadros.

**Observação:** uma mesma porta pode ter **vários endereços MAC** na tabela, como acontece quando ela está ligada a outro switch.

#### 5.5.5 Comunicação com Redes Remotas

O switch só entrega quadros dentro da rede local. Quando o destino está em **outra rede**, o quadro não vai direto ao dispositivo remoto: ele é enviado ao **roteador da rede local**, chamado de **gateway padrão**, que encaminha os dados para a outra rede.

- **IP de destino** → continua sendo o IP do **dispositivo remoto**;
- **MAC de destino** → passa a ser o MAC do **gateway padrão**.

## 6. Camada de Rede

Para levar dados **entre redes diferentes**, entra a **camada de rede**, a camada 3 do modelo OSI.

Seus principais protocolos são o **IPv4 e o IPv6**; também fazem parte dela protocolos de roteamento, como o OSPF (Open Shortest Path First), e de mensagens, como o ICMP (Internet Control Message Protocol).

### 6.1 Operações da Camada de Rede

Para levar os dados de um host até outro, atravessando os limites entre redes, a camada de rede executa quatro operações básicas:

1. **endereçamento**: cada dispositivo final recebe um endereço IP exclusivo que o identifica;
2. **encapsulamento**: na origem, os dados recebidos da camada superior são colocados em um **pacote**, que recebe um cabeçalho IP com os endereços de origem e de destino;
3. **roteamento**: quando o destino está em outra rede, os roteadores escolhem o melhor caminho e encaminham o pacote até lá;
4. **desencapsulamento**: no destino, o host confere se o endereço IP de destino é o seu; se for, remove o cabeçalho IP e entrega os dados à camada superior.

Cada roteador pelo qual o pacote passa até chegar ao destino é chamado de **salto (hop)**.

#### Entendendo o Encapsulamento e o Desencapsulamento

Um é o processo inverso do outro:

- **na origem (encapsulamento)** → Segmento + cabeçalho IP = **Pacote**;
- **no destino (desencapsulamento)** → Pacote − cabeçalho IP = **Segmento**, que é entregue à camada de transporte.

Portanto, **o encapsulamento acontece na origem, e o desencapsulamento acontece no destino**.

#### 6.1.1 Camada de Rede × Camada de Transporte

Acima da camada de rede fica a **camada de transporte** (camada 4), que organiza a comunicação entre os programas que estão sendo executados em cada host. A diferença entre as duas é:

- a camada de transporte cuida da comunicação entre aplicações;
- a camada de rede cuida do transporte dos pacotes de um host a outro, sem analisar o conteúdo que eles carregam.

Por não depender do conteúdo, a camada de rede consegue transportar qualquer tipo de comunicação.

### 6.2 Encapsulamento IP

A unidade de dados da camada de transporte é chamada de **segmento**. O IP encapsula o segmento, acrescentando a ele um cabeçalho IP, e o resultado é o **pacote IP**.

Como cada camada encapsula por conta própria, **uma pode evoluir sem afetar as outras**.

Durante o caminho:

- os roteadores e os switches de camada 3 examinam o cabeçalho IP para decidir o encaminhamento;
- os endereços IP de origem e de destino permanecem os mesmos do início ao fim;
- a parte de dados do pacote não é alterada.

A única exceção aos endereços é o **NAT (Network Address Translation – Tradução de Endereços de Rede)**, recurso do IPv4 que substitui o endereço de origem para permitir que vários dispositivos compartilhem um único endereço público.

### 6.3 Características do IP

O IP tem **baixa sobrecarga**: faz só o necessário para levar o pacote; controle de fluxo e confiabilidade ficam com o **TCP**.

Suas características básicas são três: sem conexão, melhor esforço e independente do meio.

#### 6.3.1 Sem Conexão

O IP não estabelece uma conexão com o destino antes de enviar os pacotes, e não há troca prévia de informações de controle.

É como enviar uma carta sem avisar o destinatário com antecedência.

#### 6.3.2 Melhor Esforço

O IP não garante que o pacote será entregue. Por isso, é considerado **não confiável**.

Sem uma conexão estabelecida, o emissor não sabe se o destino está ativo nem se recebeu o pacote. Os pacotes podem:

- chegar corrompidos;
- chegar fora de ordem;
- não chegar.

O IP não retransmite pacotes perdidos; isso fica com as camadas superiores, como o TCP.

#### 6.3.3 Independente do Meio

O IP funciona igual em **cobre, fibra ou rádio**; quem prepara o pacote para cada meio é a camada de enlace.

#### 6.3.4 MTU e Fragmentação

Há uma característica do meio que o IP leva em conta: a **MTU (Maximum Transmission Unit – Unidade Máxima de Transmissão)**, que é o maior tamanho de pacote que um meio consegue transportar. A camada de enlace informa a MTU à camada de rede, que define o tamanho dos pacotes.

Se o meio seguinte tem MTU menor, o roteador divide o pacote IPv4: é a **fragmentação**, que aumenta a latência.

**Importante:** os roteadores **não fragmentam pacotes IPv6**.

### 6.4 Pacote IPv4

O cabeçalho IPv4 tem as informações para entregar o pacote até a próxima parada do caminho.

#### 6.4.1 Campos do Cabeçalho IPv4

| Campo | Tamanho | Função |
| --- | --- | --- |
| Versão | 4 bits | Identifica a versão do IP; vale 0100 no IPv4 |
| Serviços Diferenciados (DS ou DiffServ) | 8 bits | Define a prioridade do pacote (antigo Tipo de Serviço – ToS); 6 bits DSCP e 2 bits ECN |
| Tempo de Vida (TTL – Time to Live) | 8 bits | Limita a vida do pacote; diminui 1 a cada roteador |
| Protocolo | 8 bits | Indica o protocolo transportado: ICMP (1), TCP (6) e UDP (17) |
| Soma de verificação do cabeçalho (checksum) | 16 bits | Detecta erros no cabeçalho |
| Endereço IPv4 de origem | 32 bits | Endereço de quem enviou; sempre unicast |
| Endereço IPv4 de destino | 32 bits | Endereço de quem vai receber; pode ser unicast, multicast ou broadcast |

#### 6.4.2 Tempo de Vida (TTL)

O TTL evita que um pacote circule para sempre na rede:

1. a origem define um valor inicial;
2. cada roteador diminui o valor em 1;
3. se o valor chegar a zero, o roteador descarta o pacote e avisa a origem com uma mensagem ICMP de "tempo excedido".

Como o TTL muda a cada salto, cada roteador também precisa recalcular a soma de verificação do cabeçalho.

#### 6.4.3 Outros Campos

- **Tamanho do Cabeçalho (IHL), Tamanho Total e Soma de Verificação**: identificam e validam o pacote;
- **Identificação, Flags e Deslocamento do Fragmento**: reorganizam um pacote que foi fragmentado. O bit **DF (Don't Fragment)**, nas flags, indica que o pacote **não deve ser fragmentado**;
- **Opções e Preenchimento**: raramente são usados.

O cabeçalho IPv4 tem 20 bytes, podendo chegar a 60 bytes quando o campo Opções é usado.

### 6.5 Limitações do IPv4

O IPv4 ainda é muito usado, mas enfrenta três grandes problemas:

- **esgotamento dos endereços**: existem cerca de 4 bilhões de endereços IPv4, quantidade insuficiente para o número crescente de dispositivos conectados;
- **falta de conectividade de ponta a ponta**: com o NAT, vários dispositivos compartilham um endereço público, e o endereço interno de cada um fica oculto. Isso atrapalha tecnologias que precisam de comunicação direta entre os hosts;
- **maior complexidade da rede**: o NAT foi criado como solução temporária, mas acrescenta complexidade, aumenta a latência e dificulta a solução de problemas.

### 6.6 IPv6

O IPv6 foi desenvolvido pela **IETF (Internet Engineering Task Force)** nos anos 1990. Suas principais melhorias são:

- **espaço de endereçamento muito maior**: endereços de 128 bits, contra 32 bits do IPv4;
- **processamento mais eficiente dos pacotes**: cabeçalho simplificado, com menos campos;
- **eliminação da necessidade de NAT**: como há endereços públicos suficientes, cada dispositivo pode ter o seu.

#### 6.6.1 Quantidade de Endereços

| Versão | Tamanho do endereço | Quantidade de endereços |
| --- | --- | --- |
| IPv4 | 32 bits | Cerca de 4,3 bilhões (4.294.967.296) |
| IPv6 | 128 bits | Cerca de 340 undecilhões |

Para ter uma ideia, a quantidade de endereços IPv6 é comparável ao número de grãos de areia da Terra.

### 6.7 Pacote IPv6

O cabeçalho IPv6 tem **tamanho fixo de 40 bytes** (maior por causa dos endereços de 128 bits), mas é **mais simples**.

#### 6.7.1 Campos do Cabeçalho IPv6

| Campo | Tamanho | Função | Equivalente no IPv4 |
| --- | --- | --- | --- |
| Versão | 4 bits | Identifica a versão; vale 0110 no IPv6 | Versão |
| Classe de Tráfego | 8 bits | Define a prioridade do pacote | Serviços Diferenciados |
| Etiqueta de Fluxo (Flow Label) | 20 bits | Indica que pacotes com a mesma etiqueta devem receber o mesmo tratamento | Não existe |
| Comprimento da Carga Útil | 16 bits | Tamanho dos dados, sem contar o cabeçalho | Tamanho Total |
| Próximo Cabeçalho | 8 bits | Indica o protocolo transportado | Protocolo |
| Limite de Saltos (Hop Limit) | 8 bits | Diminui 1 a cada roteador; em zero, o pacote é descartado | TTL |
| Endereço IPv6 de origem | 128 bits | Endereço de quem enviou | Endereço de origem |
| Endereço IPv6 de destino | 128 bits | Endereço de quem vai receber | Endereço de destino |

#### 6.7.2 Diferenças Importantes em Relação ao IPv4

- O IPv6 não tem soma de verificação do cabeçalho, pois essa função já é feita nas camadas inferior e superior. Assim, os roteadores não precisam recalculá-la a cada salto, o que melhora o desempenho;
- quando o Limite de Saltos chega a zero, o roteador envia uma mensagem ICMPv6 de "tempo excedido" para a origem;
- o pacote pode ter **cabeçalhos de extensão (EH – Extension Headers)**, opcionais, posicionados entre o cabeçalho e os dados, usados para fragmentação, segurança e mobilidade;
- os roteadores **não fragmentam** pacotes IPv6. Quando a fragmentação é necessária, ela é feita pela origem, usando um **cabeçalho de extensão**.

### 6.8 Comparativo entre os Cabeçalhos IPv4 e IPv6

| Característica | IPv4 | IPv6 |
| --- | --- | --- |
| Tamanho do endereço | 32 bits | 128 bits |
| Tamanho do cabeçalho | Variável: 20 a 60 bytes | Fixo: 40 bytes |
| Soma de verificação do cabeçalho | Sim | Não |
| Fragmentação pelo roteador | Sim | Não |
| Controle de vida do pacote | TTL | Limite de Saltos |
| Necessidade de NAT | Sim, por falta de endereços | Não |

## 7. Estrutura do Endereço IPv4

O endereço IPv4 é um endereço hierárquico de 32 bits, formado por uma porção de rede e uma porção de host.

### 7.1 Porções de Rede e de Host

- **Porção de rede**: os bits devem ser iguais em todos os dispositivos da mesma rede.
- **Porção de host**: os bits devem ser exclusivos para cada host dentro da rede.

Se dois hosts têm a mesma sequência de bits na porção de rede, eles estão na mesma rede.

O endereço, por si só, não mostra onde termina a porção de rede e onde começa a porção de host. Essa informação é dada pela máscara de sub-rede.

### 7.2 Máscara de Sub-rede

A **máscara de sub-rede** é um valor de 32 bits que indica quais bits do endereço IPv4 pertencem à porção de rede.

Ela é formada por uma sequência contínua de bits 1, seguida de uma sequência contínua de bits 0:

- os bits 1 marcam a porção de rede;
- os bits 0 marcam a porção de host.

Exemplo: a máscara 255.255.255.0 corresponde a 11111111.11111111.11111111.00000000. Os três primeiros octetos são rede, e o último é host.

A máscara não contém a rede nem o host: ela apenas indica ao dispositivo onde procurar cada parte.

#### 7.2.1 Configuração IPv4 de um Host

Para se comunicar, um host precisa ter configurados:

- **endereço IPv4**: o endereço exclusivo do host. Exemplo: 192.168.10.10;
- **máscara de sub-rede**: indica a porção de rede. Exemplo: 255.255.255.0;
- **gateway padrão**: o endereço do roteador da rede local, usado para alcançar outras redes. Exemplo: 192.168.10.1;
- **servidor DNS**: o serviço que converte nomes, como www.cisco.com, em endereços IP.

#### 7.2.2 Visualizando a Configuração IP no Windows

No Windows, essas informações podem ser vistas de duas formas:

- **comando ipconfig** → mostra o **endereço IPv4, a máscara e o gateway padrão** de cada placa de rede;
- **comando ipconfig /all** → mostra também o **endereço MAC** (chamado de "endereço físico"), os **servidores DNS** e se o endereço foi recebido por **DHCP**;
- **Central de Rede e Compartilhamento** → tela do Painel de Controle que mostra as redes ativas, se a conexão é **com fio ou sem fio** e as propriedades de cada conexão.

No Linux, o comando equivalente é **ip address**; no macOS, é **ifconfig**.

### 7.3 Comprimento do Prefixo

O **comprimento do prefixo** é a forma curta da máscara: **a quantidade de bits 1** que ela tem.

Ele é escrito em **notação de barra**: uma barra seguida do número de bits 1, logo após o endereço e sem espaço.

Exemplo: 192.168.10.10 com máscara 255.255.255.0 é escrito como **192.168.10.10/24**.

O endereço de rede também é chamado de **prefixo** ou **prefixo de rede**.

| Máscara de sub-rede | Binário | Prefixo |
| --- | --- | --- |
| 255.0.0.0 | 11111111.00000000.00000000.00000000 | /8 |
| 255.255.0.0 | 11111111.11111111.00000000.00000000 | /16 |
| 255.255.255.0 | 11111111.11111111.11111111.00000000 | /24 |
| 255.255.255.128 | 11111111.11111111.11111111.10000000 | /25 |
| 255.255.255.192 | 11111111.11111111.11111111.11000000 | /26 |
| 255.255.255.224 | 11111111.11111111.11111111.11100000 | /27 |
| 255.255.255.240 | 11111111.11111111.11111111.11110000 | /28 |
| 255.255.255.248 | 11111111.11111111.11111111.11111000 | /29 |
| 255.255.255.252 | 11111111.11111111.11111111.11111100 | /30 |

### 7.4 Operação AND

O dispositivo descobre o endereço de rede por meio do **AND lógico**, uma das três operações da lógica booleana (as outras são OR e NOT).

O AND compara dois bits e só resulta em 1 quando os dois bits são 1:

| Bit A | Bit B | A AND B |
| --- | --- | --- |
| 1 | 1 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 0 |

Na lógica digital, 1 representa verdadeiro e 0 representa falso. O resultado só é verdadeiro quando as duas entradas são verdadeiras.

#### 7.4.1 Como Encontrar o Endereço de Rede

Fazendo o AND, bit a bit, entre o endereço IPv4 e a máscara de sub-rede, obtém-se o endereço de rede.

Exemplo: host 192.168.10.10 com máscara 255.255.255.0.

|  | 1º octeto | 2º octeto | 3º octeto | 4º octeto |
| --- | --- | --- | --- | --- |
| Endereço (192.168.10.10) | 11000000 | 10101000 | 00001010 | 00001010 |
| Máscara (255.255.255.0) | 11111111 | 11111111 | 11111111 | 00000000 |
| Resultado do AND | 11000000 | 10101000 | 00001010 | 00000000 |
| Endereço de rede | 192 | 168 | 10 | 0 |

O host pertence à rede **192.168.10.0/24**.

Na prática, onde a máscara tem 255, o octeto do endereço se repete; onde a máscara tem 0, o resultado é 0.

### 7.5 Endereços de uma Rede

Dentro de cada rede existem três tipos de endereço:

- **endereço de rede**: todos os bits de host iguais a 0. Representa a rede inteira e não pode ser atribuído a um dispositivo. Exemplo: 192.168.10.0/24;
- **endereços de host**: os endereços entre o de rede e o de broadcast, que podem ser atribuídos aos dispositivos. Exemplo: 192.168.10.1 a 192.168.10.254;
- **endereço de broadcast**: todos os bits de host iguais a 1. Usado para enviar uma mensagem a todos os hosts da rede. Exemplo: 192.168.10.255.

#### 7.5.1 Quantidade de Hosts

Primeiro, descobre-se quantos bits são de host: **bits de host = 32 − prefixo**. Exemplo: em /24, são 32 − 24 = **8 bits de host**.

A quantidade de endereços de host é calculada pela fórmula 2ⁿ − 2, em que n é o número de bits de host. Subtraem-se 2 porque o endereço de rede e o de broadcast não podem ser usados por dispositivos.

| Prefixo | Bits de host | Hosts disponíveis |
| --- | --- | --- |
| /24 | 8 | 2⁸ − 2 = 254 |
| /25 | 7 | 2⁷ − 2 = 126 |
| /26 | 6 | 2⁶ − 2 = 62 |
| /27 | 5 | 2⁵ − 2 = 30 |
| /28 | 4 | 2⁴ − 2 = 14 |
| /29 | 3 | 2³ − 2 = 6 |
| /30 | 2 | 2² − 2 = 2 |

#### 7.5.2 Exemplo Completo

Endereço 192.168.10.77/27.

1. a máscara /27 é 255.255.255.224; o último octeto da máscara é 11100000;
2. o último octeto do endereço é 77 = 01001101;
3. AND: 01001101 AND 11100000 = 01000000 = 64;
4. endereço de rede: **192.168.10.64**;
5. com 5 bits de host, a rede tem 32 endereços (64 a 95);
6. broadcast: **192.168.10.95**;
7. hosts: **192.168.10.65 a 192.168.10.94** (30 hosts).

## 8. Resolução de Endereços (ARP)

Para montar o quadro, o host precisa do **MAC de destino**, que normalmente ainda não conhece.

No IPv4, essa descoberta é feita pelo **ARP (Address Resolution Protocol – Protocolo de Resolução de Endereços)**, que descobre o endereço MAC de um dispositivo local a partir do seu endereço IPv4.

### 8.1 Funcionamento do ARP

O ARP tem duas funções básicas:

- resolver endereços IPv4 em endereços MAC;
- manter uma tabela com essas associações.

#### 8.1.1 Endereços MAC no Quadro

Todo quadro Ethernet leva dois endereços MAC:

- **MAC de origem**: o da placa de rede do host que envia;
- **MAC de destino**: o do dispositivo de destino, quando ele está na mesma rede local.

Quando o destino está em outra rede, o quadro não é enviado diretamente ao destino. Ele é enviado ao **gateway padrão**, que é o roteador da rede local, responsável por encaminhar os pacotes para outras redes. Nesse caso, o MAC de destino do quadro é o MAC do roteador.

#### 8.1.2 Tabela ARP

A **tabela ARP**, também chamada de **cache ARP**, fica armazenada temporariamente na memória RAM e relaciona cada endereço IPv4 a um endereço MAC. Cada linha da tabela é chamada de **mapeamento**.

Antes de montar o quadro, o host consulta essa tabela:

- **destino na mesma rede** → procura o IPv4 do **próprio destino**;
- **destino em outra rede** → procura o IPv4 do **gateway padrão**.

Se encontrar o endereço, usa o MAC correspondente. Se não encontrar, envia uma solicitação ARP.

#### 8.1.3 Solicitação e Resposta ARP

O processo ocorre da seguinte forma:

1. **solicitação ARP**: o host envia uma mensagem perguntando qual é o MAC de determinado endereço IPv4. Como ainda não sabe o MAC do destino, envia a solicitação em broadcast (MAC de destino FF-FF-FF-FF-FF-FF), e todos os dispositivos da rede local a recebem;
2. cada dispositivo compara o IPv4 da solicitação com o seu próprio. Quem não tem aquele endereço descarta a mensagem;
3. **resposta ARP**: o dispositivo que tem o endereço responde com o seu MAC. Como já sabe quem perguntou, envia a resposta em unicast, apenas para o host que fez a solicitação;
4. o host registra o mapeamento na sua tabela ARP e envia o quadro.

As mensagens ARP são encapsuladas diretamente no quadro Ethernet, com o campo EtherType igual a 0x806. Elas não usam um pacote IPv4.

![A solicitação ARP chega a todos (broadcast); só o dono do endereço responde, diretamente a quem perguntou (unicast)](img/dispositivos/arp.png){width=6in}


| Campo do quadro | Solicitação ARP | Resposta ARP |
| --- | --- | --- |
| MAC de destino | FF-FF-FF-FF-FF-FF (broadcast) | MAC de quem fez a solicitação (unicast) |
| MAC de origem | MAC de quem pergunta | MAC de quem responde |
| Tipo (EtherType) | 0x806 | 0x806 |

**Importante:** o roteador **não encaminha broadcasts** entre suas interfaces. Por isso, a solicitação ARP **fica restrita à rede local**.

**Observação:** se nenhum dispositivo responder, o MAC não é descoberto e o pacote **não pode ser encapsulado** no quadro Ethernet para aquele destino.

#### 8.1.4 Remoção de Entradas

Entradas não usadas são removidas por um temporizador; no Windows, ficam entre **15 e 45 segundos**.

As entradas também podem ser removidas manualmente por comando. Depois da remoção, o processo de solicitação e resposta precisa acontecer de novo.

Também existem **entradas ARP estáticas**, configuradas manualmente, que **não expiram** e só saem da tabela quando são removidas por comando.

#### 8.1.5 Visualizando a Tabela ARP

| Dispositivo | Comando |
| --- | --- |
| Roteador Cisco | show ip arp |
| PC com Windows | arp -a |

### 8.2 Problemas do ARP

#### 8.2.1 Excesso de Broadcasts

Como toda solicitação ARP é um broadcast, todos os dispositivos da rede local a recebem e processam.

O impacto costuma ser pequeno, mas pode haver queda de desempenho quando **muitos dispositivos ligam ao mesmo tempo**.

#### 8.2.2 Falsificação e Envenenamento ARP

Na **falsificação ARP (ARP spoofing)**, um atacante responde a uma solicitação ARP de um endereço que pertence a outro dispositivo, como o gateway padrão, informando o seu próprio MAC.

O host que recebe a resposta falsa grava o MAC errado na tabela ARP e passa a enviar os pacotes para o atacante. Esse ataque é chamado de **envenenamento ARP (ARP poisoning)**.

Switches corporativos oferecem uma proteção chamada **DAI (Dynamic ARP Inspection – Inspeção Dinâmica de ARP)**.

### 8.3 ARP e IPv6

O IPv6 não usa ARP. Nele, a descoberta do endereço MAC é feita pelo **ND (Neighbor Discovery – Descoberta de Vizinhos)**, que usa mensagens ICMPv6.

### 8.4 Resumo do Processo ARP

| Etapa | Mensagem | Tipo de envio | Quem recebe |
| --- | --- | --- | --- |
| 1 | Solicitação ARP: "qual é o MAC deste IPv4?" | Broadcast | Todos os dispositivos da rede local |
| 2 | Resposta ARP: "o MAC é este" | Unicast | Apenas o host que perguntou |
| 3 | Registro na tabela ARP | — | O host que perguntou guarda o mapeamento |

## 9. Camada de Transporte

A **camada de transporte** (camada 4) é responsável pela **comunicação lógica entre as aplicações** de hosts diferentes: ela sabe **para qual programa** vão os dados e, no caso do TCP, **garante que eles cheguem**.

Ela liga a camada de aplicação às camadas inferiores, sem precisar conhecer o meio físico, o caminho ou o tamanho da rede.

A camada de transporte possui dois protocolos:

- **TCP (Transmission Control Protocol – Protocolo de Controle de Transmissão)**;
- **UDP (User Datagram Protocol – Protocolo de Datagrama do Usuário)**.

### 9.1 Responsabilidades da Camada de Transporte

- **Rastrear as conversas**: cada fluxo de dados entre uma aplicação de origem e uma de destino é uma **conversa**, acompanhada separadamente. Um host pode ter várias conversas ao mesmo tempo;
- **Segmentar e remontar os dados**: os dados da aplicação são divididos em blocos menores, chamados **segmentos** (TCP) ou **datagramas** (UDP), e remontados no destino;
- **Adicionar um cabeçalho**: cada bloco recebe um cabeçalho com as informações necessárias para gerenciar a comunicação e remontar os dados;
- **Identificar as aplicações**: cada aplicação que usa a rede recebe um **número de porta**, que permite entregar os dados ao programa certo;
- **Multiplexar as conversas**: como os dados são divididos em blocos, conversas diferentes podem ser intercaladas na mesma rede, sem que uma delas, como um vídeo, ocupe toda a largura de banda.

### 9.2 TCP e UDP: Visão Geral

#### 9.2.1 TCP: Confiável

O TCP **garante que todos os dados cheguem ao destino**, à custa de um cabeçalho maior e de mais processamento.

Ele estabelece uma conexão antes de enviar os dados: é **orientado à conexão**.

Ele é como enviar encomendas com rastreamento: o cliente acompanha a entrega de cada pacote do pedido.

#### 9.2.2 UDP: Rápido e Simples

O UDP **não oferece confiabilidade nem controle de fluxo**; em troca, tem cabeçalho menor e é **mais rápido**.

Suas características são:

- **sem conexão**: não estabelece uma conexão antes do envio;
- **sem estado (stateless)**: não acompanha o que foi enviado e recebido;
- **melhor esforço**: não confirma se os dados chegaram.

Ele é como enviar uma carta comum, sem registro: o remetente não sabe se ela chegou.

### 9.3 Números de Porta

Tanto o TCP quanto o UDP usam **números de porta** para gerenciar várias conversas ao mesmo tempo e entregar os dados à aplicação certa. O cabeçalho dos dois protocolos tem:

- **porta de origem**: identifica a aplicação de origem no host local. No cliente, é gerada dinamicamente, e cada nova solicitação recebe uma porta diferente;
- **porta de destino**: identifica o serviço solicitado no servidor. Exemplo: a porta 80 indica que o cliente quer o serviço Web.

#### 9.3.1 Socket

O **socket** é a combinação **endereço IP + número de porta** e identifica um processo em um host.

A combinação do socket do cliente com o socket do servidor forma um **par de sockets**, que identifica a conversa de forma única.

Exemplo: um PC (192.168.1.5) acessa um servidor Web (192.168.1.7).

- socket do cliente: 192.168.1.5:1099;
- socket do servidor: 192.168.1.7:80;
- par de sockets: 192.168.1.5:1099, 192.168.1.7:80.

Uma segunda conexão do mesmo PC, por exemplo FTP, usaria outra porta de origem (1305) e a porta 21, sem se misturar com a primeira.

A porta de origem funciona como um endereço de retorno: quando a resposta chega, a camada de transporte sabe a qual aplicação entregá-la.

#### 9.3.2 Grupos de Portas

Os números de porta têm 16 bits, ou seja, vão de 0 a 65.535. A **IANA (Internet Assigned Numbers Authority)** é a organização que os atribui e os divide em três grupos:

| Grupo | Faixa | Uso |
| --- | --- | --- |
| Portas bem conhecidas | 0 a 1.023 | Serviços comuns, como Web, e-mail e acesso remoto |
| Portas registradas | 1.024 a 49.151 | Atribuídas a aplicações específicas a pedido de uma empresa. Exemplo: 1812, para o servidor de autenticação RADIUS |
| Portas privadas ou dinâmicas (efêmeras) | 49.152 a 65.535 | Atribuídas automaticamente ao cliente quando ele inicia uma conexão |

**Observação:** alguns sistemas operacionais usam portas registradas, em vez de dinâmicas, como porta de origem.

#### 9.3.3 Portas Bem Conhecidas

| Porta | Transporte | Serviço |
| --- | --- | --- |
| 20 | TCP | FTP – dados |
| 21 | TCP | FTP – controle |
| 22 | TCP | SSH (acesso remoto seguro) |
| 23 | TCP | Telnet (acesso remoto sem criptografia) |
| 25 | TCP | SMTP (envio de e-mail) |
| 53 | UDP e TCP | DNS (resolução de nomes) |
| 67 | UDP | DHCP – servidor |
| 68 | UDP | DHCP – cliente |
| 69 | UDP | TFTP (transferência simples de arquivos) |
| 80 | TCP | HTTP (páginas Web) |
| 110 | TCP | POP3 (recebimento de e-mail) |
| 143 | TCP | IMAP (recebimento de e-mail) |
| 161 | UDP | SNMP (gerenciamento de rede) |
| 443 | TCP | HTTPS (páginas Web seguras) |

**Importante:** o DNS usa **UDP** nas consultas dos clientes, mas usa **TCP** na comunicação entre servidores DNS e quando a resposta passa de 512 bytes.

#### 9.3.4 Comando netstat

O comando **netstat** lista as **conexões ativas** do host (protocolo, endereços e portas locais e remotos, estado) e ajuda a identificar conexões desconhecidas, que podem indicar uma ameaça. A opção **netstat -n** mostra endereços e portas em forma numérica.

### 9.4 TCP em Detalhe

#### 9.4.1 Serviços do TCP

Além de segmentar e remontar os dados, o TCP oferece quatro serviços:

- **estabelecimento de sessão**: negocia uma conexão com o destino antes de enviar os dados;
- **entrega confiável**: garante que cada segmento enviado chegue ao destino, retransmitindo os perdidos;
- **entrega na mesma ordem**: numera os segmentos para remontá-los na ordem correta, mesmo que cheguem fora de ordem;
- **controle de fluxo**: ajusta a quantidade de dados enviados à capacidade do receptor, evitando sobrecarga e retransmissões.

O TCP é **stateful (com estado)**: registra o que foi enviado e o que foi confirmado, do início ao fim da sessão.

#### 9.4.2 Cabeçalho TCP

O TCP adiciona 20 bytes (160 bits) de cabeçalho aos dados da aplicação, organizados em dez campos:

| Campo | Tamanho | Função |
| --- | --- | --- |
| Porta de origem | 16 bits | Identifica a aplicação de origem |
| Porta de destino | 16 bits | Identifica a aplicação de destino |
| Número de sequência | 32 bits | Permite remontar os dados na ordem correta |
| Número de confirmação | 32 bits | Indica o próximo byte que o receptor espera |
| Tamanho do cabeçalho (data offset) | 4 bits | Indica o tamanho do cabeçalho TCP |
| Reservado | 6 bits | Reservado para uso futuro |
| Bits de controle (flags) | 6 bits | Indicam a função do segmento |
| Tamanho da janela | 16 bits | Quantidade de bytes que podem ser enviados antes de uma confirmação |
| Checksum | 16 bits | Verifica erros no cabeçalho e nos dados |
| Urgente | 16 bits | Indica se há dados urgentes |

#### 9.4.3 Bits de Controle (Flags)

Os seis bits de controle indicam o andamento da conexão. Cada um pode estar ligado ou desligado:

- **SYN** → sincroniza os números de sequência no **início da conexão**;
- **ACK** → **confirma** o recebimento; usado na abertura e no encerramento;
- **FIN** → indica que o emissor não tem mais dados; usado no **encerramento**;
- **RST** → **reinicia** a conexão quando ocorre um erro ou o tempo se esgota;
- **PSH** → função push, que pede a entrega imediata dos dados;
- **URG** → indica que o campo Urgente é válido.

#### 9.4.4 Portas no Servidor TCP

Cada aplicação do servidor usa um número de porta. Dois serviços não podem usar a mesma porta no mesmo protocolo de transporte.

Uma porta com um serviço ativo é chamada de **porta aberta**: a camada de transporte aceita os segmentos endereçados a ela.

Exemplo: dois clientes acessam o mesmo servidor.

|  | Cliente 1 (Web) | Cliente 2 (e-mail) |
| --- | --- | --- |
| Porta de origem da solicitação | 49152 (dinâmica) | 51152 (dinâmica) |
| Porta de destino da solicitação | 80 (HTTP) | 25 (SMTP) |
| Porta de origem da resposta | 80 | 25 |
| Porta de destino da resposta | 49152 | 51152 |

**Importante:** na resposta, o servidor **inverte** as portas de origem e de destino da solicitação.

#### 9.4.5 Estabelecimento da Conexão: Handshake de Três Vias

O TCP é **full-duplex**: cada conexão tem duas sessões, uma em cada sentido. Para abri-las, é usado o **handshake de três vias (three-way handshake)**:

1. **SYN**: o cliente pede para abrir a sessão cliente → servidor;
2. **SYN-ACK**: o servidor confirma essa sessão e pede para abrir a sessão servidor → cliente;
3. **ACK**: o cliente confirma a sessão servidor → cliente.

**SYN → SYN-ACK → ACK**

![O handshake de três vias abre as duas sessões de uma conexão TCP full-duplex](img/dispositivos/handshake.png){width=6in}


O handshake:

- confirma que o dispositivo de destino está presente na rede;
- verifica se o destino tem um serviço ativo na porta solicitada;
- avisa o destino de que o cliente quer abrir uma sessão naquela porta.

#### 9.4.6 Encerramento da Sessão

Para encerrar, cada sentido da conexão é fechado com um FIN e um ACK. Por isso, são necessárias quatro trocas:

1. **FIN**: o cliente avisa que não tem mais dados;
2. **ACK**: o servidor confirma;
3. **FIN**: o servidor avisa que também terminou;
4. **ACK**: o cliente confirma, e a conexão é encerrada.

Qualquer um dos dois lados pode iniciar o encerramento.

### 9.5 Confiabilidade e Controle de Fluxo do TCP

#### 9.5.1 Números de Sequência: Entrega Ordenada

O **número de sequência** indica a posição do primeiro byte de dados de cada segmento.

Na abertura é definido um **número de sequência inicial (ISN)**, aleatório; a cada envio, ele aumenta conforme os bytes transmitidos.

No destino, os segmentos ficam em um **buffer de recepção** e só são entregues à aplicação **na ordem correta**.

#### 9.5.2 Confirmação e Retransmissão

O **número de confirmação (ACK)** indica o próximo byte que o destino espera receber. Esse modelo é chamado de **confirmação antecipatória**.

O TCP usa temporizadores: se um segmento não é confirmado a tempo, ele é retransmitido.

Exemplo: o host A envia os segmentos 1 a 10, e se perdem os segmentos 3 e 4.

- **sem SACK**: o host B só consegue informar que espera o segmento 3. O host A reenvia do 3 ao 10, duplicando os segmentos 5 a 10;
- **com SACK (Selective Acknowledgment – Confirmação Seletiva)**: o host B informa que recebeu 1 e 2 e, seletivamente, de 5 a 10. O host A reenvia apenas os segmentos 3 e 4.

O SACK é opcional e negociado no handshake de três vias.

#### 9.5.3 Tamanho da Janela

O **tamanho da janela** é a quantidade de bytes que o destino consegue receber e processar de uma vez, ou seja, quantos bytes a origem pode enviar antes de esperar uma confirmação.

Ele é definido no handshake e vai em todos os segmentos, então **o destino pode reduzi-lo** quando o buffer enche.

Exemplo: o PC B define uma janela de 10.000 bytes. O PC A pode enviar até o byte 10.000 sem confirmação. Quando o PC B confirma até o byte 2.920 (ACK 2.921), a janela do PC A avança para o byte 12.920.

Esse avanço contínuo é a **janela deslizante**.

#### 9.5.4 Tamanho Máximo do Segmento (MSS)

O **MSS (Maximum Segment Size)** é a maior quantidade de dados, em bytes, que um dispositivo aceita em um único segmento TCP, sem contar o cabeçalho. Ele é informado no handshake.

O cálculo parte da MTU da Ethernet:

**MTU (1500 bytes) − cabeçalho IPv4 (20 bytes) − cabeçalho TCP (20 bytes) = MSS de 1460 bytes**

#### 9.5.5 Prevenção de Congestionamento

Quando a rede congestiona, os roteadores descartam pacotes, e retransmitir sem controle pioraria o congestionamento.

Por isso, ao perceber confirmações atrasadas, **a origem reduz** a quantidade de bytes enviados antes de cada confirmação.

É importante não confundir: no congestionamento, quem reduz o envio é a origem; já o tamanho da janela é definido pelo destino.

### 9.6 UDP em Detalhe

#### 9.6.1 Características do UDP

O UDP segmenta e remonta os dados como o TCP, mas:

- os dados são remontados na ordem em que chegam;
- os segmentos perdidos não são reenviados;
- não há estabelecimento de sessão;
- o emissor não é informado sobre a disponibilidade do destino.

Se a ordem ou a confiabilidade forem importantes, quem cuida disso é a própria aplicação.

#### 9.6.2 Cabeçalho UDP

O cabeçalho UDP tem apenas 8 bytes (64 bits) e quatro campos:

| Campo | Tamanho | Função |
| --- | --- | --- |
| Porta de origem | 16 bits | Identifica a aplicação de origem |
| Porta de destino | 16 bits | Identifica a aplicação de destino |
| Comprimento | 16 bits | Indica o tamanho do datagrama |
| Checksum | 16 bits | Verifica erros no cabeçalho e nos dados |

#### 9.6.3 Portas no Servidor UDP

Assim como no TCP, os servidores UDP usam portas bem conhecidas ou registradas, e o cliente usa uma porta de origem dinâmica. O mesmo par de portas é usado em toda a transação, e na resposta as portas são invertidas.

Exemplo: consulta DNS para a porta 53, com porta de origem 49152 → a resposta sai da porta 53 para a 49152.

### 9.7 Escolha do Protocolo de Transporte

#### 9.7.1 Quando Usar o TCP

**Quando todos os dados precisam chegar, completos e em ordem.**

Exemplos: navegadores (HTTP e HTTPS), e-mail (SMTP, POP3, IMAP), transferência de arquivos (FTP), acesso remoto (SSH, Telnet), bancos de dados e acesso a contas bancárias.

Também em vídeos armazenados (filmes sob demanda): o "carregando" (buffering) é o TCP restabelecendo a transmissão.

#### 9.7.2 Quando Usar o UDP

Há três tipos de aplicação adequados ao UDP:

- **vídeo e multimídia ao vivo** → toleram pequenas perdas, mas **não toleram atrasos**. Exemplos: VoIP e transmissões ao vivo;
- **solicitação e resposta simples** → a transação é pequena, e **se não houver resposta basta repetir o pedido**. Exemplos: DNS e DHCP;
- **aplicações que cuidam da própria confiabilidade** → não precisam dos controles do TCP ou fazem esses controles por conta própria. Exemplos: SNMP e TFTP.

### 9.8 Comparativo entre TCP e UDP

| Característica | TCP | UDP |
| --- | --- | --- |
| Conexão | Orientado à conexão | Sem conexão |
| Estado da sessão | Stateful (com estado) | Stateless (sem estado) |
| Confiabilidade | Garante a entrega e retransmite | Melhor esforço, sem retransmissão |
| Ordem dos dados | Reordena pelos números de sequência | Entrega na ordem de chegada |
| Controle de fluxo | Sim (janela deslizante) | Não |
| Cabeçalho | 20 bytes, 10 campos | 8 bytes, 4 campos |
| Velocidade | Menor | Maior |
| Unidade de dados | Segmento | Datagrama |
| Exemplos | HTTP, HTTPS, FTP, SMTP, SSH | DNS, DHCP, VoIP, TFTP, SNMP |

## 10. Serviços de Endereçamento IP: DNS e DHCP

Dois serviços da camada de aplicação facilitam o uso dos endereços IP:

- o **DNS**, que permite usar nomes em vez de números para chegar aos servidores;
- o **DHCP**, que configura automaticamente o endereço IP dos dispositivos.

Sem eles, seria preciso memorizar endereços numéricos e configurar manualmente cada dispositivo de uma rede.

### 10.1 DNS (Domain Name System)

O **DNS (Domain Name System – Sistema de Nomes de Domínio)** associa nomes de domínio a endereços IP.

Um nome como www.cisco.com, chamado de **FQDN (Fully Qualified Domain Name – Nome de Domínio Totalmente Qualificado)**, é muito mais fácil de lembrar que o endereço 198.133.219.25.

Se o endereço do servidor mudar, o usuário não percebe: o nome continua o mesmo.

#### 10.1.1 Funcionamento do DNS

1. o usuário digita um FQDN no navegador;
2. o computador envia uma consulta DNS ao servidor DNS configurado nele;
3. o servidor DNS encontra o endereço IP correspondente ao nome;
4. a resposta com o endereço IP volta ao computador;
5. o computador usa esse endereço IP para acessar o servidor.

**Nome → Consulta DNS → Endereço IP → Acesso ao servidor**

Normalmente, o endereço do servidor DNS é fornecido pelo provedor de Internet (ISP).

#### 10.1.2 Registros DNS

O servidor DNS armazena **registros de recursos**, que contêm o nome, o endereço e o tipo do registro. Os principais tipos são:

| Registro | Função |
| --- | --- |
| A | Endereço IPv4 de um dispositivo |
| AAAA | Endereço IPv6 de um dispositivo (pronuncia-se "quad-A") |
| NS | Servidor de nomes autoritativo, responsável pelo domínio |
| MX | Servidor de troca de e-mail do domínio |

#### 10.1.3 Resolução e Cache

Quando recebe uma consulta, o servidor DNS:

1. procura o nome nos seus próprios registros;
2. se não encontrar, consulta outros servidores DNS;
3. ao obter a resposta, guarda o endereço temporariamente (em cache), para responder mais rápido se o mesmo nome for consultado de novo.

Os computadores com Windows também guardam os nomes já resolvidos. O comando **ipconfig /displaydns** mostra as entradas DNS em cache.

#### 10.1.4 Formato da Mensagem DNS

O DNS usa um único formato de mensagem para consultas, respostas, mensagens de erro e troca de registros entre servidores:

| Seção | Conteúdo |
| --- | --- |
| Pergunta | A consulta feita ao servidor de nomes |
| Resposta | Os registros que respondem à pergunta |
| Autoridade | Os registros que apontam para o servidor responsável |
| Adicional | Os registros com informações complementares |

#### 10.1.5 Hierarquia DNS

O DNS é organizado de forma hierárquica, a partir dos nomes de domínio. A estrutura é dividida em **zonas** menores, e cada servidor DNS é responsável apenas pela sua zona.

Consultas de outras zonas são encaminhadas ao servidor responsável; por ser distribuído, o DNS é **escalável**.

Os **domínios de nível superior (TLD – Top-Level Domain)** são a **parte final do nome, depois do último ponto**, e indicam o tipo de organização ou o país:

- .com: empresas e indústria;
- .org: organizações sem fins lucrativos;
- .br: Brasil;
- .au: Austrália.

#### Entendendo a Resolução de Nomes Passo a Passo

Com a hierarquia, uma consulta a www.cisco.com percorre o seguinte caminho:

1. o sistema operacional verifica primeiro o **cache DNS local**;
2. se não encontrar, consulta o **servidor DNS recursivo** (o servidor DNS configurado no host), que verifica o próprio cache;
3. se ele também não souber, pergunta ao **servidor raiz (root)**, que indica qual servidor TLD consultar;
4. o **servidor TLD** (no exemplo, o do .com) indica o servidor autoritativo do domínio;
5. o **servidor autoritativo**, que tem os registros definitivos do domínio, informa o endereço IP;
6. o servidor recursivo **guarda a resposta em cache** e a devolve ao cliente, que também pode guardá-la.

**Cache local → Servidor recursivo → Raiz → TLD → Autoritativo → Resposta**

#### 10.1.6 Comando nslookup

O **nslookup** é um utilitário que permite consultar manualmente um servidor DNS para resolver um nome.

Ao ser executado, ele mostra o servidor DNS padrão configurado no host. Em seguida, basta digitar o nome desejado.

Ele é usado para identificar problemas de resolução de nomes e verificar o funcionamento dos servidores DNS.

### 10.2 DHCP (Dynamic Host Configuration Protocol)

O **DHCP (Dynamic Host Configuration Protocol – Protocolo de Configuração Dinâmica de Host)** atribui automaticamente o endereço IPv4, a máscara de sub-rede, o gateway padrão, o servidor DNS e outros parâmetros aos dispositivos.

#### 10.2.1 Endereçamento Estático e Dinâmico

- **Endereçamento estático**: o administrador digita manualmente as informações de IP em cada dispositivo;
- **Endereçamento dinâmico**: o DHCP fornece essas informações automaticamente.

Muitas redes usam os dois:

- DHCP para os dispositivos dos usuários, como computadores e celulares;
- endereçamento estático para os dispositivos de rede, como roteadores, switches, servidores e impressoras, que precisam manter sempre o mesmo endereço.

O DHCP é preferido em redes grandes ou com muitos usuários novos, e **reduz os erros** da configuração manual.

#### 10.2.2 Pool e Período de Concessão

O servidor DHCP escolhe os endereços de uma lista configurada, chamada **pool** ou **escopo**.

O endereço é emprestado por um tempo determinado, chamado **período de concessão (lease)**. O endereço volta ao pool para ser reutilizado quando:

- o período de concessão termina; ou
- o servidor recebe uma mensagem DHCPRELEASE, enviada pelo cliente que libera o endereço.

O servidor DHCP garante que o mesmo endereço não seja atribuído a dois dispositivos ao mesmo tempo.

#### 10.2.3 Quem Pode Ser Servidor DHCP

- em redes médias e grandes: normalmente um servidor dedicado;
- em redes domésticas: o roteador que conecta a casa ao provedor;
- nos provedores de Internet: a maioria usa DHCP para atribuir endereços aos clientes.

**Observação:** o mesmo roteador doméstico pode ter **dois papéis ao mesmo tempo**:

- **servidor DHCP** → para os dispositivos da rede local;
- **cliente DHCP** → na interface **WAN**, ligada ao provedor, de quem recebe um **endereço IPv4 público**.

#### 10.2.4 Mensagens DHCP

O cliente obtém o endereço em quatro etapas:

1. **DHCPDISCOVER**: ao se conectar, o cliente envia em broadcast uma mensagem para encontrar um servidor DHCP;
2. **DHCPOFFER**: o servidor oferece uma concessão, com o endereço IPv4, a máscara, o gateway padrão, o servidor DNS e a duração da concessão;
3. **DHCPREQUEST**: o cliente aceita uma das ofertas, identificando o servidor escolhido (pode haver mais de um servidor na rede);
4. **DHCPACK**: o servidor confirma a concessão.

**DHCPDISCOVER → DHCPOFFER → DHCPREQUEST → DHCPACK**

![Processo DORA: as quatro mensagens com que o cliente obtém um endereço IPv4](img/dispositivos/dora.png){width=6in}


Se a oferta não for mais válida, o servidor responde com **DHCPNAK** (confirmação negativa), e o cliente recomeça o processo.

Antes de a concessão vencer, o cliente precisa renová-la com uma nova mensagem DHCPREQUEST.

#### 10.2.5 DHCPv6

O **DHCPv6** oferece serviços parecidos para o IPv6. As diferenças são:

- o DHCPv6 não fornece o gateway padrão, que é obtido pela mensagem **Anúncio de Roteador (RA – Router Advertisement)**, enviada pelo roteador;
- as principais mensagens são SOLICIT, ADVERTISE, REQUEST (ou INFORMATION REQUEST, no DHCPv6 sem estado) e REPLY.

### 10.3 Comparativo entre DNS e DHCP

| Característica | DNS | DHCP |
| --- | --- | --- |
| Função | Converter nomes em endereços IP | Configurar automaticamente os dispositivos |
| O que o cliente envia | Um nome de domínio | Um pedido de configuração |
| O que recebe | O endereço IP do nome | IP, máscara, gateway e DNS |
| Transporte e porta | UDP 53 (TCP 53 entre servidores) | UDP 67 (servidor) e 68 (cliente) |
| Comando útil | nslookup, ipconfig /displaydns | ipconfig /all |

## 11. A Linha de Comando do Cisco IOS

O sistema operacional dos roteadores e switches Cisco é o **Cisco IOS (Internetwork Operating System)**.

O IOS pode ser configurado por uma interface gráfica (GUI) ou pela **CLI (Command Line Interface – Interface de Linha de Comando)**, que é um programa em texto para digitar comandos que configuram, monitoram e administram os dispositivos.

A CLI dá **mais controle que a interface gráfica** e é praticamente a mesma em switches e roteadores.

### 11.1 Acesso à CLI

O acesso à CLI pode ser feito de duas formas:

- **fora da banda (out-of-band)**: por uma conexão direta, como o cabo ligado à **porta de console** do equipamento. Não depende da rede estar funcionando e é usado na configuração inicial;
- **dentro da banda (in-band)**: pela própria rede, usando protocolos de acesso remoto como **SSH** (seguro, com criptografia) ou **Telnet** (sem criptografia).

Quando o dispositivo termina de iniciar, aparece o prompt (por exemplo, Router>), e a CLI está pronta para receber comandos.

### 11.2 Modos de Comando

Por segurança, o IOS **separa o acesso em modos**, e cada modo permite um conjunto diferente de comandos.

**Importante:** **o prompt mostra em qual modo o usuário está**: **>** → EXEC do usuário; **#** → EXEC privilegiado; **(config)#** → configuração.

#### 11.2.1 Modo EXEC do Usuário

- permite apenas comandos básicos de monitoramento;
- não permite alterar a configuração;
- é chamado de modo "somente visualização";
- prompt terminado em **>**: Switch> ou Router>.

#### 11.2.2 Modo EXEC Privilegiado

- permite acesso a todos os comandos e recursos, incluindo os de gerenciamento;
- é o único modo a partir do qual se entra nos modos de configuração;
- prompt terminado em **#**: Switch# ou Router#.

#### 11.2.3 Modo de Configuração Global

O **modo de configuração global** é o modo em que se alteram as configurações que afetam o dispositivo inteiro. Seu prompt é **Switch(config)#**.

A partir dele, acessam-se os **submodos de configuração**, usados para configurar partes específicas:

- **modo de configuração de linha**: configura o acesso pelo console, pelo SSH ou pelo Telnet. Prompt: Switch(config-line)#;
- **modo de configuração de interface**: configura uma porta do switch ou uma interface do roteador. Prompt: Switch(config-if)#.

| Modo | Prompt | O que permite |
| --- | --- | --- |
| EXEC do usuário | Switch> | Monitoramento básico |
| EXEC privilegiado | Switch# | Todos os comandos de visualização e gerenciamento |
| Configuração global | Switch(config)# | Configurações do dispositivo inteiro |
| Configuração de linha | Switch(config-line)# | Acesso por console, SSH e Telnet |
| Configuração de interface | Switch(config-if)# | Configuração de portas e interfaces |

#### 11.2.4 Navegação entre os Modos

| Comando | De onde | Para onde |
| --- | --- | --- |
| enable | EXEC do usuário | EXEC privilegiado |
| disable | EXEC privilegiado | EXEC do usuário |
| configure terminal | EXEC privilegiado | Configuração global |
| line console 0 | Configuração global | Configuração de linha (console) |
| interface nome | Configuração global | Configuração de interface |
| exit | Qualquer submodo | Um nível acima |
| end ou Ctrl+Z | Qualquer modo de configuração | EXEC privilegiado |

**Switch> → enable → Switch# → configure terminal → Switch(config)# → interface → Switch(config-if)#**

### 11.3 Estrutura dos Comandos

Cada comando do IOS tem uma sintaxe própria e só pode ser executado no modo adequado. A estrutura geral é o comando seguido de palavras-chave e argumentos:

- **palavra-chave**: parâmetro predefinido no sistema. Exemplo: em show ip protocols, "ip protocols" são palavras-chave;
- **argumento**: valor definido pelo usuário. Exemplo: em ping 192.168.10.5, o endereço é o argumento.

Depois de digitar o comando completo, pressiona-se Enter para executá-lo.

#### 11.3.1 Convenções de Sintaxe

A documentação da Cisco usa as seguintes convenções para mostrar como um comando deve ser digitado:

| Convenção | Significado |
| --- | --- |
| **negrito** | Comandos e palavras-chave digitados exatamente como aparecem |
| *itálico* | Argumentos cujo valor é fornecido pelo usuário |
| \[x\] | Elemento opcional |
| {x} | Elemento obrigatório |
| \[x {y \| z}\] | Escolha obrigatória dentro de um elemento opcional |

Exemplos:

- **description** *texto*: descreve a finalidade de uma interface. Exemplo: description Conecta ao switch principal da matriz;
- **ping** *endereço-ip*: testa a comunicação. Exemplo: ping 10.10.10.5;
- **traceroute** *endereço-ip*: mostra o caminho até o destino. Exemplo: traceroute 192.168.254.254.

A **Referência de Comandos do Cisco IOS** é a fonte oficial de informações sobre cada comando.

#### 11.3.2 Ajuda da CLI

A CLI tem um sistema de ajuda que usa o ponto de interrogação (**?**):

- **ajuda contextual**: digitar **?** mostra os comandos disponíveis no modo atual; digitar o início de um comando seguido de ? (exemplo: cl?) mostra os comandos que começam com essas letras; digitar um comando seguido de espaço e ? mostra as palavras-chave e os argumentos que podem vir a seguir;
- **verificação de sintaxe**: quando um comando é digitado de forma errada, o IOS mostra uma mensagem indicando o problema, como comando ambíguo, incompleto ou incorreto.

#### 11.3.3 Abreviações

Comandos e palavras-chave podem ser abreviados até o menor número de letras que os identifique de forma única.

Exemplo: **configure** vira **conf**; já **con** não funciona, porque mais de um comando começa assim.

#### 11.3.4 Teclas de Atalho

| Tecla | Função |
| --- | --- |
| Tab | Completa um comando digitado parcialmente |
| Seta para cima ou Ctrl+P | Mostra os comandos anteriores do histórico |
| Seta para baixo ou Ctrl+N | Avança no histórico |
| Ctrl+A | Leva o cursor ao início da linha |
| Ctrl+E | Leva o cursor ao final da linha |
| Seta para a esquerda ou Ctrl+B | Move o cursor um caractere para a esquerda |
| Seta para a direita ou Ctrl+F | Move o cursor um caractere para a direita |
| Esc B / Esc F | Move o cursor uma palavra para a esquerda / para a direita |
| Backspace | Apaga o caractere à esquerda do cursor |
| Ctrl+D | Apaga o caractere sob o cursor |
| Ctrl+K | Apaga do cursor até o final da linha |
| Ctrl+U ou Ctrl+X | Apaga do cursor até o início da linha |
| Ctrl+W | Apaga a palavra à esquerda do cursor |
| Esc D | Apaga do cursor até o final da palavra |
| Ctrl+R, Ctrl+I ou Ctrl+L | Mostra de novo o prompt e a linha após uma mensagem do sistema |

**Observação:** a CLI do IOS **não reconhece a tecla Delete**.

Quando a saída de um comando não cabe na tela, aparece o aviso **--More--**:

- **Enter** → mostra a **próxima linha**;
- **Espaço** → mostra a **próxima tela**;
- **qualquer outra tecla** → encerra a exibição.

Para interromper operações:

- **Ctrl+C ou Ctrl+Z** → saem de qualquer modo de configuração e voltam ao **EXEC privilegiado**;
- **Ctrl+Shift+6** → **interrompe** processos como pesquisas DNS, ping e traceroute.

### 11.4 Comandos show

Os comandos **show** exibem a **configuração e o estado** do dispositivo.

| Comando | Para que serve |
| --- | --- |
| show running-config | Mostrar a configuração atual em uso |
| show interfaces | Verificar o estado das interfaces e as mensagens de erro |
| show ip interface | Verificar as informações de camada 3 de uma interface |
| show arp | Ver os hosts conhecidos nas LANs Ethernet locais (tabela ARP) |
| show ip route | Ver as informações de roteamento |
| show protocols | Ver quais protocolos estão funcionando |
| show version | Ver a memória, as interfaces e as licenças do dispositivo |

## 12. Configuração de uma Rede Cisco Pequena

Com a CLI, é possível fazer a configuração inicial de switches e roteadores. Ela envolve quatro tarefas principais:

- dar um nome ao dispositivo;
- proteger o acesso com senhas;
- configurar um endereço IP para gerenciamento;
- salvar a configuração.

### 12.1 Elementos da Configuração Básica

#### 12.1.1 Nome do Dispositivo

O **nome de host (hostname)** é o nome configurado no equipamento; de preferência, **indica onde ele está instalado**.

Exemplo: SW\_Predio\_R-Sala\_216.

Depois de configurado, o nome aparece no prompt. Exemplo: R1#.

#### 12.1.2 Senhas

Cada forma de acesso à CLI deve ser protegida por senha. Os requisitos mínimos são:

- senha no acesso pelo console;
- senha no acesso remoto (Telnet e SSH), configurado nas **linhas VTY (Virtual Terminal)**;
- senha no modo EXEC privilegiado, que é o modo em que a configuração pode ser alterada.

**Importante:** o **Telnet** envia o nome de usuário e a senha em **texto simples** e não é seguro. O **SSH** criptografa essas informações e é o método recomendado.

#### 12.1.3 Arquivos de Configuração

O dispositivo guarda duas configurações:

- **running-config** → configuração **em uso**, na memória **RAM**. **É perdida** se o equipamento for desligado;
- **startup-config** → configuração **salva**, na **NVRAM** (memória não volátil), carregada quando o equipamento é ligado.

Por isso, depois de cada alteração, a configuração deve ser salva com o comando **copy running-config startup-config**.

### 12.2 Configuração Básica do Switch

#### 12.2.1 Comandos da Configuração Inicial

| Tarefa | Comandos |
| --- | --- |
| Configurar o nome | hostname nome |
| Proteger o modo EXEC do usuário (console) | line console 0 / password senha / login |
| Proteger o acesso remoto (Telnet/SSH) | line vty 0 15 / password senha / login |
| Proteger o modo EXEC privilegiado | enable secret senha |
| Criptografar todas as senhas do arquivo de configuração | service password-encryption |
| Exibir um aviso legal | banner motd # mensagem # |
| Configurar a interface de gerenciamento | interface vlan 1 / ip address endereço máscara / no shutdown |
| Salvar a configuração | copy running-config startup-config |

O comando **login** faz o dispositivo pedir a senha ao acessar aquela linha. O **banner motd** (message of the day) exibe uma mensagem a quem tenta acessar o equipamento.

#### 12.2.2 Interface Virtual do Switch (SVI)

O switch de camada 2 **só precisa de IP para ser gerenciado remotamente** (Telnet, SSH ou HTTP).

Esse endereço é configurado na **SVI (Switch Virtual Interface – Interface Virtual do Switch)**, que é uma interface virtual, e não uma porta física. Por padrão, é usada a **VLAN 1**.

```
S1(config)# interface vlan 1
S1(config-if)# ip address 192.168.1.20 255.255.255.0
S1(config-if)# no shutdown
S1(config-if)# exit
S1(config)# ip default-gateway 192.168.1.1
```

- **interface vlan 1**: entra na configuração da SVI;
- **ip address**: define o endereço IPv4 e a máscara;
- **no shutdown**: ativa a interface;
- **ip default-gateway**: define o gateway padrão, necessário para gerenciar o switch a partir de outra rede.

### 12.3 Configuração Inicial do Roteador

#### 12.3.1 Etapas

A configuração inicial do roteador segue sete etapas:

1. configurar o nome do dispositivo;
2. proteger o modo EXEC privilegiado;
3. proteger o modo EXEC do usuário;
4. proteger o acesso remoto Telnet/SSH;
5. criptografar todas as senhas do arquivo de configuração;
6. exibir o aviso legal;
7. salvar a configuração.

#### 12.3.2 Exemplo

```
Router(config)# hostname R1
R1(config)# enable secret class
R1(config)# line console 0
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# exit
R1(config)# line vty 0 4
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# transport input ssh telnet
R1(config-line)# exit
R1(config)# service password-encryption
R1(config)# banner motd # Acesso permitido somente a usuarios autorizados #
R1(config)# end
R1# copy running-config startup-config
```

**Observação:** o comando transport input apenas **permite** as conexões SSH; para o SSH funcionar, também são necessários o domínio IP, as chaves RSA e um usuário local com login local.

A senha do modo EXEC privilegiado deve ser forte, porque esse modo dá acesso total à configuração.

#### 12.3.3 Configuração das Interfaces do Roteador

Para que o roteador funcione como gateway de cada rede, cada interface recebe um endereço IP da rede a que está conectada e precisa ser ativada:

```
R1(config)# interface g0/0/0
R1(config-if)# description Conecta a LAN 192.168.10.0
R1(config-if)# ip address 192.168.10.1 255.255.255.0
R1(config-if)# no shutdown
```

**Importante:** as interfaces do roteador ficam **desativadas por padrão**; por isso, o comando **no shutdown** é obrigatório.

### 12.4 Proteção dos Dispositivos

#### 12.4.1 Recomendações de Senha

- usar pelo menos 8 caracteres, de preferência 10 ou mais;
- misturar letras maiúsculas e minúsculas, números, símbolos e espaços;
- evitar repetições, palavras do dicionário, sequências, nomes de usuários, parentes ou animais e datas de nascimento;
- escrever palavras com erros propositais. Exemplo: Security = 5ecur1ty;
- trocar as senhas periodicamente;
- não anotar as senhas nem deixá-las em locais visíveis.

| Senha | Força | Motivo |
| --- | --- | --- |
| secret | Fraca | Palavra simples do dicionário |
| toyota | Fraca | Nome de uma marca |
| bob1967 | Fraca | Nome e ano de nascimento |
| Blueleaf23 | Fraca | Palavras e números simples |
| b67n42d39c | Forte | Mistura letras e números |
| 12^h u4@1p7 | Forte | Mistura letras, números, símbolos e espaço |

Nos roteadores Cisco, os espaços depois do primeiro caractere contam na senha, o que permite usar uma **frase secreta (passphrase)**: mais longa e mais fácil de lembrar.

O **nome de usuário** também merece cuidado:

- evitar o nome completo ou informações pessoais;
- não repetir a mesma combinação de usuário e senha em contas diferentes;
- não dar pistas da senha nem do cargo ou local de trabalho.

#### 12.4.2 Acesso Remoto Seguro

- o acesso pelo console é usado principalmente na configuração inicial;
- o acesso pela rede, por SSH ou Telnet, é chamado de conexão VTY e também precisa de senha.

Quantidade de linhas VTY:

- **switches Cisco** → em geral, **16 linhas (0 a 15)**;
- **roteadores** → em geral, **5 linhas (0 a 4)**.

Todas as linhas VTY disponíveis devem ter senha, que pode ser a mesma para todas.

As senhas definidas com **password** (console e VTY) ficam na running-config em **texto simples**; as definidas com **secret** já são gravadas com hash. O comando **service password-encryption** criptografa as que estão em texto simples.

#### 12.4.3 Configuração do SSH

Antes de configurar o SSH, o dispositivo precisa ter um nome de host exclusivo e conectividade de rede.

1. **verificar o suporte**: o comando **show ip ssh** confirma se o IOS suporta SSH;
2. **configurar o domínio IP**: **ip domain-name** cisco.com;
3. **gerar as chaves RSA**: **crypto key generate rsa**. A geração das chaves ativa o SSH automaticamente. O sistema pede o tamanho da chave (por exemplo, 1024 bits); chaves maiores são mais seguras, mas demoram mais;
4. **criar um usuário local**: **username** admin **secret** ccna;
5. **configurar as linhas VTY**: **line vty 0 15**, depois **transport input ssh** (aceita somente SSH, bloqueando o Telnet) e **login local** (usa o usuário local para autenticar);
6. **ativar a versão 2**: **ip ssh version 2**. Por padrão, o SSH aceita as versões 1 e 2 (aparece como 1.99), mas a versão 1 tem falhas de segurança conhecidas.

```
S1(config)# ip domain-name cisco.com
S1(config)# crypto key generate rsa
How many bits in the modulus [512]: 1024
S1(config)# username admin secret ccna
S1(config)# line vty 0 15
S1(config-line)# transport input ssh
S1(config-line)# login local
S1(config-line)# exit
S1(config)# ip ssh version 2
```

Para apagar as chaves RSA, usa-se **crypto key zeroize rsa**, o que desativa o SSH automaticamente.

#### Entendendo as Chaves RSA

As chaves RSA usam **criptografia assimétrica**, que trabalha com **duas chaves diferentes**:

- **chave pública** → pode ser compartilhada e é usada para **criptografar**;
- **chave privada** → fica em segredo e é a única que consegue **descriptografar**.

Funciona como uma caixa de correio: qualquer pessoa pode colocar uma carta pela abertura (chave pública), mas só o dono tem a chave para abrir e ler (chave privada). Por isso, o comando crypto key generate rsa gera um **par de chaves**.

Na **criptografia simétrica**, ao contrário, a **mesma chave** criptografa e descriptografa. Ela é mais rápida, mas exige que a chave seja compartilhada com segurança.

O SSH **combina os dois tipos**: usa o par de chaves RSA para **autenticar o dispositivo e combinar uma chave de sessão**, e a criptografia simétrica para **cifrar os dados da sessão**.

#### 12.4.4 Verificação do SSH

No computador, um cliente SSH como o **PuTTY** se conecta ao IP da SVI na **porta 22**, com o usuário e a senha configurados.

No dispositivo:

- **show ip ssh**: mostra a versão e a configuração do SSH;
- **show ssh**: mostra as conexões SSH ativas.

### 12.5 Gateway Padrão

O **gateway padrão** é o endereço da interface do roteador ligada à rede local. Ele é usado somente quando o destino está em outra rede.

O host e o gateway padrão devem estar **na mesma rede**.

#### 12.5.1 Gateway Padrão no Host

Exemplo: o roteador R1 conecta duas redes.

- interface G0/0/0: rede 192.168.10.0/24, com PC1 e PC2;
- interface G0/0/1: rede 192.168.11.0/24, com PC3 e PC4.

Casos:

- **PC1 para PC2 (mesma rede)** → o gateway **não é usado**; o pacote vai direto ao PC2 pelo switch;
- **PC1 para PC3 (outra rede)** → o pacote leva o IP do PC3, mas é **entregue ao gateway padrão** (interface G0/0/0 do R1). O roteador consulta sua **tabela de roteamento**, que lista as redes que ele conhece e por qual interface alcançá-las, e envia o pacote pela G0/0/1 até o PC3.

No IPv6, o processo é o mesmo, usando o endereço IPv6 do roteador local.

#### 12.5.2 Gateway Padrão no Switch

Para ser gerenciado a partir de outra rede, o switch também precisa de um gateway padrão:

```
S1(config)# ip default-gateway 192.168.10.1
```

Exemplo: um administrador de outra rede acessa o S1 por SSH; para **responder**, o S1 precisa do gateway padrão, senão a resposta não sai da rede local.

No IPv6, o switch recebe o gateway automaticamente pela mensagem de Anúncio de Roteador (ICMPv6), sem configuração manual.

### 12.6 Resumo dos Comandos de Configuração

| Comando | Modo | Função |
| --- | --- | --- |
| hostname | Configuração global | Define o nome do dispositivo |
| enable secret | Configuração global | Senha criptografada do modo EXEC privilegiado |
| line console 0 | Configuração global | Entra na linha do console |
| line vty | Configuração global | Entra nas linhas de acesso remoto |
| password / login | Configuração de linha | Define e exige a senha da linha |
| transport input ssh | Configuração de linha | Aceita somente SSH |
| login local | Configuração de linha | Autentica com o usuário local |
| service password-encryption | Configuração global | Criptografa as senhas |
| banner motd | Configuração global | Exibe o aviso legal |
| interface vlan 1 | Configuração global | Entra na SVI do switch |
| ip address | Configuração de interface | Define endereço e máscara |
| no shutdown | Configuração de interface | Ativa a interface |
| ip default-gateway | Configuração global | Define o gateway padrão do switch |
| ip domain-name | Configuração global | Define o domínio, necessário para o SSH |
| crypto key generate rsa | Configuração global | Gera as chaves e ativa o SSH |
| username ... secret | Configuração global | Cria um usuário local |
| ip ssh version 2 | Configuração global | Usa somente a versão 2 do SSH |
| copy running-config startup-config | EXEC privilegiado | Salva a configuração |

## 13. ICMP e Testes de Conectividade

Os testes de conectividade usam o **ICMP (Internet Control Message Protocol – Protocolo de Mensagens de Controle da Internet)**, que envia **mensagens de erro e informativas** sobre os pacotes IP.

Esse retorno, porém, **não torna o IP confiável**.

As mensagens ICMP não são obrigatórias e muitas vezes são bloqueadas por segurança.

Existem duas versões:

- **ICMPv4**: usado com o IPv4;
- **ICMPv6**: usado com o IPv6, com os mesmos serviços e funções adicionais.

### 13.1 Mensagens Comuns ao ICMPv4 e ao ICMPv6

#### 13.1.1 Acessibilidade do Host (Eco)

Para testar se um host está acessível, o host local envia uma solicitação de eco (Echo Request). Se o destino estiver disponível, ele devolve uma resposta de eco (Echo Reply).

Essa troca de mensagens é a base do comando ping.

#### 13.1.2 Destino ou Serviço Inalcançável

Quando um host ou um roteador recebe um pacote que não consegue entregar, envia à origem uma mensagem de destino inalcançável, com um código que indica o motivo.

| Código | ICMPv4 | ICMPv6 |
| --- | --- | --- |
| 0 | Rede inalcançável | Nenhuma rota para o destino |
| 1 | Host inalcançável | Comunicação proibida administrativamente (por exemplo, por um firewall) |
| 2 | Protocolo inalcançável | Além do escopo do endereço de origem |
| 3 | Porta inalcançável | Endereço inalcançável |
| 4 | — | Porta inalcançável |

#### 13.1.3 Tempo Excedido

Quando o TTL de um pacote IPv4 chega a zero, o roteador descarta o pacote e envia à origem uma mensagem de tempo excedido.

No IPv6 acontece o mesmo, mas com base no campo Limite de Saltos.

As mensagens de tempo excedido são usadas pelo traceroute.

### 13.2 Mensagens Exclusivas do ICMPv6

O ICMPv6 inclui o **ND (Neighbor Discovery – Descoberta de Vizinhos)**, que tem quatro mensagens, divididas em dois grupos.

#### 13.2.1 Entre Roteador e Dispositivo

- **RS (Router Solicitation – Solicitação de Roteador)**: enviada pelo dispositivo para pedir informações de endereçamento ao roteador;
- **RA (Router Advertisement – Anúncio de Roteador)**: enviada pelo roteador a cada 200 segundos, ou em resposta a uma RS, com informações como o prefixo da rede, o comprimento do prefixo, o endereço DNS e o nome de domínio.

Um host que se configura automaticamente pelo método **SLAAC (Stateless Address Autoconfiguration – Configuração Automática de Endereço sem Estado)**, ou seja, que monta o próprio endereço a partir das informações da RA, usa como gateway padrão o endereço do roteador que enviou a RA.

#### 13.2.2 Entre Dispositivos

- **NS (Neighbor Solicitation – Solicitação de Vizinho)**;
- **NA (Neighbor Advertisement – Anúncio de Vizinho)**.

Essas mensagens têm duas funções:

- **resolução de endereços**: substitui o ARP no IPv6. O dispositivo conhece o IPv6 do destino, mas não o MAC; envia uma NS, e o dono do endereço responde com uma NA contendo seu MAC;
- **DAD (Duplicate Address Detection – Detecção de Endereço Duplicado)**: ao receber um endereço, o dispositivo envia uma NS para o próprio endereço. Se alguém responder com uma NA, o endereço já está em uso; se ninguém responder, o endereço é exclusivo. O DAD não é obrigatório, mas é recomendado.

O ND também tem uma mensagem de redirecionamento, semelhante à do ICMPv4.

| Mensagem | Quem envia | Para quê |
| --- | --- | --- |
| RS | Dispositivo | Pedir informações de endereçamento ao roteador |
| RA | Roteador | Informar prefixo, gateway e DNS |
| NS | Dispositivo | Descobrir o MAC de um IPv6 ou verificar se um endereço está em uso |
| NA | Dispositivo | Responder à NS informando o MAC ou que o endereço está em uso |

### 13.3 Ping

O **ping** é um utilitário que testa a conectividade entre hosts usando as mensagens de solicitação e resposta de eco. Funciona no IPv4 e no IPv6.

Mostra o tempo de cada resposta e, no final, a **taxa de sucesso** e o **tempo médio de ida e volta**.

**Observação:** é comum **o primeiro ping falhar** quando o host ainda precisa descobrir o MAC do destino (por ARP ou ND) antes de enviar a solicitação.

#### 13.3.1 Sequência de Testes com Ping

Os testes são feitos do mais próximo para o mais distante:

1. **ping no loopback**: 127.0.0.1 (IPv4) ou ::1 (IPv6). Confirma que o IP está instalado e funcionando no próprio host. Não testa o endereço, a máscara, o gateway nem as camadas inferiores. Se falhar, o TCP/IP não está funcionando no host;
2. **ping no gateway padrão**: confirma que o host e a interface do roteador estão funcionando na rede local. Se o gateway não responder, pode-se testar outro host conhecido da rede. Se esse outro host responder e o gateway não, o problema pode ser o endereço de gateway configurado errado ou um bloqueio de segurança na interface do roteador;
3. **ping em um host remoto**: confirma a comunicação na rede local, o funcionamento do gateway padrão, de todos os roteadores do caminho e do próprio host remoto.

**Observação:** muitos administradores bloqueiam as mensagens ICMP que entram na rede corporativa. Por isso, **a falta de resposta ao ping nem sempre significa falha de conexão**.

### 13.4 Traceroute

O ping informa se há comunicação, mas não mostra o caminho. O **traceroute** (no Windows, **tracert**) lista os saltos alcançados ao longo do caminho até o destino.

- se os dados chegam ao destino, a lista mostra a interface de cada roteador do caminho;
- se os dados param em algum ponto, o último roteador que respondeu indica onde está o problema ou a restrição de segurança.

#### 13.4.1 Tempo de Ida e Volta (RTT)

Para cada salto, o traceroute mostra o **RTT (Round Trip Time – Tempo de Ida e Volta)**, que é o tempo que o pacote leva para chegar ao salto e voltar.

- um asterisco (\*) indica um pacote perdido ou sem resposta;
- tempos altos ou perdas em um salto indicam que aquele roteador ou suas conexões podem estar sobrecarregados.

#### 13.4.2 Como o Traceroute Funciona

O traceroute usa o campo TTL (ou o Limite de Saltos, no IPv6) junto com a mensagem ICMP de tempo excedido:

1. envia a primeira sequência de mensagens com TTL = 1;
2. o primeiro roteador reduz o TTL para 0, descarta o pacote e responde com "tempo excedido". Assim, o traceroute descobre o endereço do primeiro salto;
3. envia nova sequência com TTL = 2, depois 3, e assim por diante, descobrindo cada salto seguinte;
4. ao chegar ao destino, o host final responde com "porta inalcançável" ou com uma resposta de eco, em vez de "tempo excedido", e o rastreamento termina.

**TTL 1 → 1º roteador responde → TTL 2 → 2º roteador responde → ... → destino responde**

![O traceroute aumenta o TTL a cada rodada; cada roteador que zera o TTL se identifica com "tempo excedido"](img/dispositivos/traceroute.png){width=6in}


### 13.5 Comparativo entre Ping e Traceroute

| Característica | Ping | Traceroute |
| --- | --- | --- |
| O que testa | Se há comunicação com o destino | Por onde os pacotes passam |
| Mensagens ICMP usadas | Solicitação e resposta de eco | Tempo excedido (e porta inalcançável ou eco no destino) |
| Informação mostrada | Taxa de sucesso e tempo médio | Cada salto e o RTT de cada um |
| Comando no Windows | ping | tracert |
| Comando no Cisco IOS e Linux | ping | traceroute |

## Glossário de Siglas

| Sigla | Nome completo | Significado |
| --- | --- | --- |
| AAAA | — | Registro DNS que associa um nome a um endereço IPv6 |
| ACK | Acknowledgment | Confirmação de recebimento (TCP e DHCP) |
| ARP | Address Resolution Protocol | Protocolo que descobre o MAC a partir do endereço IPv4 |
| bps | Bits per second | Bits por segundo, unidade da largura de banda |
| CAM | Content Addressable Memory | Memória que guarda a tabela de endereços MAC do switch |
| CIA | Confidentiality, Integrity and Availability | Tríade da segurança: confidencialidade, integridade e disponibilidade |
| CLI | Command Line Interface | Interface de linha de comando |
| CRC | Cyclic Redundancy Check | Verificação de redundância cíclica, usada para detectar erros |
| CSMA/CD | Carrier Sense Multiple Access with Collision Detection | Método de acesso ao meio com detecção de colisão (Ethernet antiga) |
| DAD | Duplicate Address Detection | Detecção de endereço IPv6 duplicado |
| DAI | Dynamic ARP Inspection | Proteção contra envenenamento ARP |
| DF | Don't Fragment | Bit do cabeçalho IPv4 que impede a fragmentação do pacote |
| DHCP | Dynamic Host Configuration Protocol | Protocolo que configura automaticamente os endereços IP |
| DNS | Domain Name System | Sistema que converte nomes de domínio em endereços IP |
| DS | Differentiated Services | Campo do IPv4 que define a prioridade do pacote |
| DSCP | Differentiated Services Code Point | Bits de prioridade dentro do campo DS |
| ECN | Explicit Congestion Notification | Bits de notificação de congestionamento no campo DS |
| EH | Extension Header | Cabeçalho de extensão opcional do IPv6 |
| FCS | Frame Check Sequence | Campo do quadro Ethernet que detecta erros |
| FIN | Finish | Flag TCP que encerra a sessão |
| FQDN | Fully Qualified Domain Name | Nome de domínio completo, como www.cisco.com |
| FTP | File Transfer Protocol | Protocolo de transferência de arquivos |
| GUI | Graphical User Interface | Interface gráfica |
| HTTP | Hypertext Transfer Protocol | Protocolo das páginas Web |
| HTTPS | Hypertext Transfer Protocol Secure | Versão segura do HTTP |
| IaaS | Infrastructure as a Service | Infraestrutura como serviço |
| IANA | Internet Assigned Numbers Authority | Organização que atribui números de porta e endereços |
| ICMP | Internet Control Message Protocol | Protocolo de mensagens de controle e erro do IP |
| IEEE | Institute of Electrical and Electronics Engineers | Instituto que mantém os padrões Ethernet e sem fio |
| IETF | Internet Engineering Task Force | Organização que desenvolve os padrões da Internet, como o IPv6 |
| IHL | Internet Header Length | Campo do IPv4 com o tamanho do cabeçalho |
| IMAP | Internet Message Access Protocol | Protocolo de recebimento de e-mail |
| IOS | Internetwork Operating System | Sistema operacional dos equipamentos Cisco |
| IP | Internet Protocol | Protocolo de endereçamento e roteamento da camada de rede |
| ISN | Initial Sequence Number | Número de sequência inicial do TCP |
| ISP | Internet Service Provider | Provedor de serviços de Internet |
| LAN | Local Area Network | Rede local |
| LLC | Logical Link Control | Subcamada de controle de enlace lógico |
| LLDP | Link Layer Discovery Protocol | Protocolo de descoberta de vizinhos na camada de enlace |
| MAC | Media Access Control | Endereço físico da placa de rede e subcamada de controle de acesso ao meio |
| MSS | Maximum Segment Size | Maior quantidade de dados aceita em um segmento TCP |
| MTU | Maximum Transmission Unit | Maior tamanho de pacote que um meio transporta |
| MX | Mail Exchange | Registro DNS do servidor de e-mail |
| NA | Neighbor Advertisement | Anúncio de vizinho (ICMPv6) |
| NAT | Network Address Translation | Tradução de endereços de rede |
| ND | Neighbor Discovery | Descoberta de vizinhos no IPv6 |
| NIC | Network Interface Card | Placa de rede |
| NS | Name Server / Neighbor Solicitation | Registro DNS do servidor autoritativo / Solicitação de vizinho (ICMPv6) |
| NVRAM | Non-Volatile Random Access Memory | Memória não volátil onde fica a startup-config |
| OSI | Open Systems Interconnection | Modelo de referência de sete camadas |
| OSPF | Open Shortest Path First | Protocolo de roteamento |
| OUI | Organizationally Unique Identifier | 3 primeiros bytes do MAC, que identificam o fabricante |
| PaaS | Platform as a Service | Plataforma como serviço |
| PDU | Protocol Data Unit | Unidade de dados de protocolo de cada camada |
| POP3 | Post Office Protocol version 3 | Protocolo de recebimento de e-mail |
| QoS | Quality of Service | Qualidade de serviço, priorização do tráfego |
| RA | Router Advertisement | Anúncio de roteador (ICMPv6) |
| RADIUS | Remote Authentication Dial-In User Service | Serviço de autenticação de usuários (porta UDP 1812) |
| RAM | Random Access Memory | Memória volátil onde fica a running-config |
| RS | Router Solicitation | Solicitação de roteador (ICMPv6) |
| RSA | Rivest-Shamir-Adleman | Algoritmo das chaves de criptografia usadas pelo SSH |
| RST | Reset | Flag TCP que reinicia a conexão |
| RTT | Round Trip Time | Tempo de ida e volta |
| SaaS | Software as a Service | Software como serviço |
| SACK | Selective Acknowledgment | Confirmação seletiva do TCP |
| SFD | Start Frame Delimiter | Delimitador de início do quadro Ethernet |
| SLAAC | Stateless Address Autoconfiguration | Configuração automática de endereço IPv6 sem estado |
| SMTP | Simple Mail Transfer Protocol | Protocolo de envio de e-mail |
| SNMP | Simple Network Management Protocol | Protocolo de gerenciamento de rede |
| SQL | Structured Query Language | Linguagem de consulta a bancos de dados |
| SSH | Secure Shell | Acesso remoto seguro, com criptografia |
| STP | Spanning Tree Protocol | Protocolo que evita loops em redes de switches |
| SVI | Switch Virtual Interface | Interface virtual do switch, usada para gerenciá-lo |
| SYN | Synchronize | Flag TCP que inicia a conexão |
| TCP | Transmission Control Protocol | Protocolo de transporte confiável, orientado à conexão |
| TFTP | Trivial File Transfer Protocol | Protocolo simples de transferência de arquivos |
| TLD | Top-Level Domain | Domínio de nível superior, como .com ou .br |
| ToS | Type of Service | Antigo nome do campo DS do IPv4 |
| TTL | Time to Live | Tempo de vida do pacote IPv4 |
| UDP | User Datagram Protocol | Protocolo de transporte rápido, sem conexão |
| VLAN | Virtual Local Area Network | Rede local virtual |
| VM | Virtual Machine | Máquina virtual |
| VoIP | Voice over IP | Voz sobre IP |
| VTY | Virtual Terminal | Linhas de acesso remoto (Telnet e SSH) |
| WAN | Wide Area Network | Rede de longa distância; interface do roteador ligada ao provedor |
| WLAN | Wireless Local Area Network | Rede local sem fio |

## Exercícios

### Parte A – Redes Confiáveis (ver item 1.6)

1. Cite as quatro características básicas de uma rede confiável.
2. Explique o que é redundância e como a comutação de pacotes ajuda a obtê-la.
3. Em uma rede congestionada, qual tráfego a QoS prioriza: uma ligação de voz ou o download de um arquivo? Justifique.
4. Relacione cada requisito de segurança à sua definição: confidencialidade, integridade e disponibilidade.

### Parte B – Design Hierárquico (ver itens 2.1 e 2.5)

1. Por que o endereço MAC é chamado de físico e o endereço IP de lógico?
2. Cite dois motivos pelos quais redes Ethernet grandes, com muitos hosts, não são eficientes.
3. Indique a camada do modelo hierárquico responsável por: conectar os usuários; transportar grandes volumes de dados rapidamente; controlar o tráfego entre as redes.

### Parte C – Nuvem e Virtualização (ver itens 3.2, 3.3 e 3.7)

1. Classifique cada serviço como SaaS, PaaS ou IaaS: um e-mail online; servidores virtuais alugados; um ambiente para desenvolver e publicar aplicações.
2. Qual tipo de nuvem é indicado para um grupo de hospitais que precisa cumprir as mesmas leis de proteção de dados?
3. Explique os problemas de "ponto único de falha" e "expansão de servidores".
4. Diferencie o hipervisor Tipo 1 do hipervisor Tipo 2.

### Parte D – Conversão de Binário para Decimal (ver item 4.1.2)

Converta para decimal:

1. 10000000
2. 11111111
3. 10101010
4. 01100100
5. 11000000.10101000.00000001.00001010

### Parte E – Conversão de Decimal para Binário (ver item 4.1.4)

Converta para binário:

1. 172
2. 224
3. 99
4. 15
5. 10.1.200.254

### Parte F – Sistema Hexadecimal (ver item 4.3.1)

1. Converta para hexadecimal: 255, 168, 10 e 192.
2. Converta para decimal: 0x1F, 0xA0 e 0xFF.
3. Quantos dígitos hexadecimais são necessários para escrever um endereço MAC? E um endereço IPv6?

### Parte G – Quadro e Endereços Ethernet (ver itens 5.3.2 e 5.4.4)

1. Qual é o tamanho mínimo e o máximo de um quadro Ethernet?
2. Que protocolo está sendo transportado quando o campo EtherType vale 0x800? E 0x86DD? E 0x806?
3. Classifique cada endereço MAC de destino como unicast, broadcast ou multicast: FF-FF-FF-FF-FF-FF; 01-00-5E-00-00-05; 00-1A-2B-3C-4D-5E; 33-33-00-00-00-01.

### Parte H – Tabela de Endereços MAC (ver itens 5.5.2 e 5.5.3)

Um switch recém-ligado tem o PC-A na porta 1, o PC-B na porta 2 e o PC-C na porta 3.

1. O PC-A envia um quadro para o PC-C. O que o switch registra na tabela e por quais portas envia o quadro?
2. O PC-C responde ao PC-A. O que o switch registra e por qual porta envia o quadro?
3. O que é um "unicast desconhecido"?

### Parte I – Cabeçalhos IPv4 e IPv6 (ver itens 6.4.1, 6.7.1 e 6.8)

1. Qual campo do IPv6 substitui o TTL do IPv4? E qual substitui o campo Protocolo?
2. Um pacote IPv4 sai do host com TTL 64 e passa por 3 roteadores. Qual é o valor do TTL ao chegar ao destino?
3. Cite três diferenças entre os cabeçalhos IPv4 e IPv6.

### Parte J – Máscara, Prefixo e Operação AND (ver itens 7.3 e 7.4.1)

1. Escreva o prefixo das máscaras: 255.255.0.0; 255.255.255.192; 255.255.255.248.
2. Escreva a máscara dos prefixos: /8; /25; /28.
3. Use a operação AND para encontrar o endereço de rede de 172.16.45.200/16.
4. Use a operação AND para encontrar o endereço de rede de 192.168.5.130/26.

### Parte K – Endereços de uma Rede (ver itens 7.5.1 e 7.5.2)

Para cada endereço, informe o endereço de rede, o primeiro host, o último host, o broadcast e a quantidade de hosts:

1. 192.168.1.100/24
2. 192.168.1.100/28
3. 10.0.0.50/29
4. 172.16.10.65/27

### Parte L – ARP (ver itens 8.1.3 e 8.4)

1. O PC1 (192.168.10.10/24) quer enviar dados para 192.168.10.20. Qual endereço IPv4 ele procura na tabela ARP?
2. E se o destino for 8.8.8.8?
3. Por que a solicitação ARP é enviada em broadcast e a resposta em unicast?
4. Qual comando mostra a tabela ARP em um PC com Windows? E em um roteador Cisco?

### Parte M – Portas e Protocolos de Transporte (ver itens 9.3.2, 9.3.3 e 9.8)

1. Indique o serviço associado a cada porta: 22, 23, 25, 53, 67, 80, 110 e 443.
2. Classifique cada porta como bem conhecida, registrada ou dinâmica: 80, 1812, 50000 e 443.
3. Indique se cada aplicação usa preferencialmente TCP ou UDP: transferência bancária; VoIP; consulta DNS; envio de e-mail; transmissão de vídeo ao vivo.
4. Escreva o par de sockets de um cliente 10.1.1.5, porta 49200, acessando um servidor HTTPS em 10.1.1.100.
5. Calcule o MSS de uma interface Ethernet com MTU de 1500 bytes usando IPv4 e TCP.

### Parte N – DNS e DHCP (ver itens 10.1.2, 10.2.4 e 10.3)

1. Qual registro DNS associa um nome a um endereço IPv6? E qual identifica o servidor de e-mail?
2. Escreva, em ordem, as quatro mensagens do DHCPv4.
3. Qual mensagem o servidor DHCP envia quando a oferta não é mais válida?
4. Qual informação o DHCPv6 não fornece e de onde ela é obtida?

### Parte O – Cisco IOS e Configuração (ver itens 11.2.4 e 12.6)

1. Identifique o modo de cada prompt: R1>; R1#; R1(config)#; R1(config-line)#; R1(config-if)#.
2. Qual comando leva do modo EXEC do usuário ao EXEC privilegiado? E do EXEC privilegiado à configuração global?
3. Qual é a diferença entre running-config e startup-config? Qual comando salva a configuração?
4. Escreva os comandos para configurar o switch S1 com o endereço de gerenciamento 192.168.1.2/24 e o gateway padrão 192.168.1.1.
5. Coloque em ordem as etapas para ativar o SSH: criar usuário local; configurar o domínio IP; gerar chaves RSA; configurar as linhas VTY; ativar a versão 2.

### Parte P – Ping e Traceroute (ver itens 13.3.1 e 13.4.2)

1. O ping para 127.0.0.1 funciona, mas o ping para o gateway padrão falha. O que esse resultado indica?
2. Coloque os testes de ping na ordem correta: host remoto; loopback; gateway padrão.
3. Explique como o traceroute usa o TTL para descobrir cada roteador do caminho.
4. O que significa um asterisco (\*) na saída do traceroute?

### Parte Q – Endereços Completos e Outros Métodos (ver itens 4.1.3, 4.1.5 e 4.3.2)

1. Converta para decimal, octeto por octeto: 11000000.10101000.00001010.01100100.
2. Converta 200.150.10.1 para binário, escrevendo a cadeia de subtrações de cada octeto.
3. Converta 0x3C para decimal pelo método de multiplicar por 16.
4. Converta 250 para hexadecimal pelo método de dividir por 16.

### Parte R – Comunicação com Redes Remotas (ver itens 5.5.5 e 12.5.1)

O PC1 tem o endereço 192.168.10.10/24 e o gateway padrão 192.168.10.1.

1. O PC1 envia dados para 192.168.11.20. Qual endereço IP de destino vai no pacote? E qual endereço MAC de destino vai no quadro?
2. E se o destino for 192.168.10.25?

### Parte S – DNS e DHCP na Prática (ver itens 10.1.5 e 10.2.3)

1. Coloque em ordem as etapas de uma consulta DNS: servidor TLD; cache local; servidor autoritativo; servidor raiz; servidor recursivo.
2. Quais são os dois papéis DHCP que um roteador doméstico pode ter ao mesmo tempo?

### Parte T – Questões Conceituais

1. Qual é a diferença entre half-duplex e full-duplex?
2. Por que o IP é chamado de "melhor esforço"? Quem garante a entrega dos dados?
3. Quais são as três etapas do handshake de três vias? E quantas trocas são necessárias para encerrar a sessão TCP?
4. Qual é a diferença entre tamanho da janela e prevenção de congestionamento no TCP?
5. Por que o Telnet não é recomendado para o acesso remoto?
6. Por que um switch de camada 2 precisa de um gateway padrão se ele não encaminha pacotes entre redes?
7. Qual é o nome do conjunto formado por confidencialidade, integridade e disponibilidade?
8. Qual é a diferença entre um firewall pessoal e um firewall de rede?
9. O que indicam os 3 primeiros bytes de um endereço MAC?
10. Qual é a diferença entre criptografia simétrica e assimétrica? Qual delas é usada nas chaves RSA do SSH?

## Gabarito

### Parte A

1. Tolerância a falhas, escalabilidade, qualidade de serviço (QoS) e segurança.
2. Redundância é ter **vários caminhos até o mesmo destino**. Na comutação de pacotes, a mensagem é dividida em pacotes que podem seguir caminhos diferentes; se um enlace falhar, os roteadores usam outro.
3. A ligação de voz, porque é **sensível ao tempo**. A QoS prioriza pelo tipo de tráfego.
4. Confidencialidade → só os autorizados leem os dados; integridade → os dados não são alterados no caminho; disponibilidade → os autorizados acessam os dados quando precisam.

### Parte B

1. O MAC é gravado na placa e **não muda**; o IP é atribuído **de acordo com a rede** e muda quando o host troca de rede.
2. Seria difícil localizar um host apenas pelo MAC, e o excesso de broadcasts consumiria a largura de banda.
3. Acesso; núcleo; distribuição.

### Parte C

1. E-mail online → SaaS; servidores virtuais alugados → IaaS; ambiente para desenvolver e publicar aplicações → PaaS.
2. Nuvem comunitária.
3. Ponto único de falha → se o servidor falha, o serviço para. Expansão de servidores → muitos servidores físicos, cada um com um serviço e boa parte do tempo ociosos, desperdiçando espaço e energia.
4. Tipo 1 → instalado direto no hardware, mais eficiente, usado em data centers. Tipo 2 → instalado sobre um sistema operacional, usado em computadores pessoais e testes.

### Parte D

| Binário | Bits 1 | Decimal |
| --- | --- | --- |
| 10000000 | 128 | **128** |
| 11111111 | 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 | **255** |
| 10101010 | 128 + 32 + 8 + 2 | **170** |
| 01100100 | 64 + 32 + 4 | **100** |

5. 11000000 = 192; 10101000 = 168; 00000001 = 1; 00001010 = 10 → **192.168.1.10**.

### Parte E

| Decimal | Subtrações | Binário |
| --- | --- | --- |
| 172 | 172 − 128 = 44 − 32 = 12 − 8 = 4 − 4 = 0 | **10101100** |
| 224 | 224 − 128 = 96 − 64 = 32 − 32 = 0 | **11100000** |
| 99 | 99 − 64 = 35 − 32 = 3 − 2 = 1 − 1 = 0 | **01100011** |
| 15 | 15 − 8 = 7 − 4 = 3 − 2 = 1 − 1 = 0 | **00001111** |

5. 10 = 00001010; 1 = 00000001; 200 = 11001000; 254 = 11111110 → **00001010.00000001.11001000.11111110**.

### Parte F

1. 255 = **FF**; 168 = **A8**; 10 = **0A**; 192 = **C0**.
2. 0x1F = (1 × 16) + 15 = **31**; 0xA0 = (10 × 16) + 0 = **160**; 0xFF = (15 × 16) + 15 = **255**.
3. MAC → **12 dígitos** (48 bits); IPv6 → **32 dígitos** (128 bits).

### Parte G

1. Mínimo de **64 bytes** e máximo de **1518 bytes**.
2. 0x800 → IPv4; 0x86DD → IPv6; 0x806 → ARP.
3. FF-FF-FF-FF-FF-FF → broadcast; 01-00-5E-00-00-05 → multicast (IPv4); 00-1A-2B-3C-4D-5E → unicast; 33-33-00-00-00-01 → multicast (IPv6).

### Parte H

1. O switch registra o **MAC do PC-A na porta 1**. Como não conhece o PC-C, envia o quadro pelas **portas 2 e 3** (unicast desconhecido).
2. O switch registra o **MAC do PC-C na porta 3** e, como já conhece o PC-A, envia o quadro **somente pela porta 1**.
3. É o quadro cujo MAC de destino não está na tabela; ele é enviado por todas as portas, exceto a de entrada.

### Parte I

1. Limite de Saltos substitui o TTL; Próximo Cabeçalho substitui o Protocolo.
2. 64 − 3 = **61**.
3. Por exemplo: endereço de 128 bits × 32 bits; cabeçalho fixo de 40 bytes × variável de 20 a 60 bytes; o IPv6 não tem checksum no cabeçalho; os roteadores não fragmentam pacotes IPv6.

### Parte J

1. 255.255.0.0 → **/16**; 255.255.255.192 → **/26**; 255.255.255.248 → **/29**.
2. /8 → **255.0.0.0**; /25 → **255.255.255.128**; /28 → **255.255.255.240**.
3. Máscara 255.255.0.0: os dois primeiros octetos se repetem e os dois últimos viram 0 → **172.16.0.0/16**.
4. Último octeto: 130 = 10000010; máscara /26 = 11000000; AND = 10000000 = 128 → **192.168.5.128/26**.

### Parte K

| Endereço | Rede | Primeiro host | Último host | Broadcast | Hosts |
|------------------|--------------|--------------|--------------|--------------|------|
| 192.168.1.100/24 | 192.168.1.0 | 192.168.1.1 | 192.168.1.254 | 192.168.1.255 | 254 |
| 192.168.1.100/28 | 192.168.1.96 | 192.168.1.97 | 192.168.1.110 | 192.168.1.111 | 14 |
| 10.0.0.50/29 | 10.0.0.48 | 10.0.0.49 | 10.0.0.54 | 10.0.0.55 | 6 |
| 172.16.10.65/27 | 172.16.10.64 | 172.16.10.65 | 172.16.10.94 | 172.16.10.95 | 30 |

Como conferir o /28: 4 bits de host → blocos de 16 endereços (0, 16, 32, 48, 64, 80, **96**, 112...). O 100 está no bloco que começa em 96 e termina em 111.

### Parte L

1. O próprio destino, **192.168.10.20**, porque está na mesma rede.
2. O **gateway padrão**, porque 8.8.8.8 está em outra rede.
3. Na solicitação, o host **ainda não sabe** o MAC do destino, então pergunta a todos (broadcast). Na resposta, o destino **já sabe** quem perguntou e responde só a ele (unicast).
4. Windows → **arp -a**; roteador Cisco → **show ip arp**.

### Parte M

1. 22 → SSH; 23 → Telnet; 25 → SMTP; 53 → DNS; 67 → DHCP (servidor); 80 → HTTP; 110 → POP3; 443 → HTTPS.
2. 80 → bem conhecida; 1812 → registrada; 50000 → dinâmica; 443 → bem conhecida.
3. Transferência bancária → TCP; VoIP → UDP; consulta DNS → UDP; envio de e-mail → TCP; vídeo ao vivo → UDP.
4. **10.1.1.5:49200, 10.1.1.100:443**.
5. 1500 − 20 − 20 = **1460 bytes**.

### Parte N

1. **AAAA**; **MX**.
2. DHCPDISCOVER → DHCPOFFER → DHCPREQUEST → DHCPACK.
3. **DHCPNAK**.
4. O **gateway padrão**, que é obtido pela mensagem de **Anúncio de Roteador (RA)**.

### Parte O

1. R1> → EXEC do usuário; R1# → EXEC privilegiado; R1(config)# → configuração global; R1(config-line)# → configuração de linha; R1(config-if)# → configuração de interface.
2. **enable**; **configure terminal**.
3. running-config → em uso, na RAM, perdida ao desligar; startup-config → salva na NVRAM. Comando: **copy running-config startup-config**.
4. Comandos:

```
S1(config)# interface vlan 1
S1(config-if)# ip address 192.168.1.2 255.255.255.0
S1(config-if)# no shutdown
S1(config-if)# exit
S1(config)# ip default-gateway 192.168.1.1
```

5. Configurar o domínio IP → gerar as chaves RSA → criar o usuário local → configurar as linhas VTY → ativar a versão 2.

### Parte P

1. O TCP/IP está funcionando no próprio host, mas há um problema na rede local: gateway configurado errado, cabo ou placa com defeito, interface do roteador com problema ou bloqueio de segurança ao ping.
2. Loopback → gateway padrão → host remoto.
3. O traceroute envia pacotes com TTL 1, 2, 3... Cada roteador que zera o TTL descarta o pacote e responde com "tempo excedido", revelando seu endereço. O destino final responde com "porta inalcançável" ou com resposta de eco.
4. Um pacote perdido ou sem resposta naquele salto.

### Parte Q

1. Octeto por octeto:

| Octeto | Bits 1 | Decimal |
| --- | --- | --- |
| 11000000 | 128 + 64 | 192 |
| 10101000 | 128 + 32 + 8 | 168 |
| 00001010 | 8 + 2 | 10 |
| 01100100 | 64 + 32 + 4 | 100 |

Resultado: **192.168.10.100**.

2. Subtrações:

| Octeto | Subtrações | Binário |
| --- | --- | --- |
| 200 | 200 − 128 = 72 − 64 = 8 − 8 = 0 | 11001000 |
| 150 | 150 − 128 = 22 − 16 = 6 − 4 = 2 − 2 = 0 | 10010110 |
| 10 | 10 − 8 = 2 − 2 = 0 | 00001010 |
| 1 | 1 − 1 = 0 | 00000001 |

Resultado: **11001000.10010110.00001010.00000001**.

3. 0x3C = (3 × 16) + 12 = 48 + 12 = **60**.
4. 250 ÷ 16 = 15, com resto 10. 15 = F e 10 = A → **FA**.

### Parte R

1. IP de destino → **192.168.11.20** (o do dispositivo remoto); MAC de destino → o **MAC do gateway padrão** (192.168.10.1).
2. Os dois são do próprio destino: IP 192.168.10.25 e o MAC dele, porque está na mesma rede.

### Parte S

1. Cache local → servidor recursivo → servidor raiz → servidor TLD → servidor autoritativo.
2. **Servidor DHCP** para a rede local e **cliente DHCP** na interface WAN, ligada ao provedor.

### Parte T

1. Half-duplex → envia **ou** recebe, um de cada vez; full-duplex → envia **e** recebe ao mesmo tempo.
2. Porque não garante a entrega nem retransmite pacotes perdidos. A entrega é garantida pelo **TCP**.
3. SYN → SYN-ACK → ACK. O encerramento precisa de **quatro trocas** (FIN, ACK, FIN, ACK).
4. O tamanho da janela é definido pelo **destino**, conforme sua capacidade; na prevenção de congestionamento, é a **origem** que reduz o envio ao perceber perdas.
5. Porque envia o usuário e a senha em **texto simples**.
6. Para poder **responder** a um administrador que o acessa a partir de outra rede; sem gateway, a resposta não sai da rede local.
7. **Tríade CIA**.
8. Firewall pessoal → protege um único dispositivo; firewall de rede → protege a rede inteira, na borda.
9. O **OUI**, que identifica o fabricante da placa.
10. Simétrica → a mesma chave criptografa e descriptografa; assimétrica → chave pública e chave privada. As chaves RSA do SSH usam **criptografia assimétrica**.
