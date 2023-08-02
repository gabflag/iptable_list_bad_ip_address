def extract_ips(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    ips = [line.split()[0] for line in lines]

    with open(output_file, 'w') as f:
        for ip in ips:
            f.write(ip + '\n')


input_file = "iplist.txt"
output_file = "bad_ips.txt"

extract_ips(input_file, output_file)

print("IPs extraídos com sucesso e salvos em 'bad_ips.txt'.")
