# iptable_list_bad_user_agent

Para criar uma regra no iptables de um servidor, é possível bloquear um único IP ou uma lista de IPs. No caso de utilizar uma lista, é necessário formatá-la corretamente.

Uma fonte interessante para coletar IPs envolvidos em atividades suspeitas é o website https://www.projecthoneypot.org/list_of_ips.php. Recomendo realizar o login para obter a lista completa.

![image](https://github.com/gabflag/iptable_list_bad_user_agent/assets/95552879/db54c48a-4ed9-4b52-8286-06431b60182d)

A fim de coletar os IPs, copie o trecho da página HTML fornecido e cole-o em um arquivo de texto com a extensão ".txt", denominado "iplist.txt". O sistema irá processar a leitura e salvar apenas os endereços de IP em um arquivo chamado "bad_ips.txt".

Segue o formato após o procedimento:

![image](https://github.com/gabflag/iptable_list_bad_user_agent/assets/95552879/034becc6-3033-4766-b906-f8d89863b7fa)

