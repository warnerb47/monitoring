def extract_hosts():
    import json
    with open('terraform-output.json') as json_file:
        data = json.load(json_file)
    # print(data['ec2_instances_created']['value'])
    hosts = {'masters': [], 'workers': []}
    ec2_instances_created = data['ec2_instances_created']['value']
    for key in ec2_instances_created:
        # print(ec2_instances_created[key]['public_ip'])
        # print(ec2_instances_created[key]['tags']['Name'])
        if('master' in ec2_instances_created[key]['tags']['Name']):
            hosts['masters'].append({
                'public_ip': ec2_instances_created[key]['public_ip'],
                'tag': ec2_instances_created[key]['tags']['Name']
            })
        else:
            hosts['workers'].append({
                'public_ip': ec2_instances_created[key]['public_ip'],
                'tag': ec2_instances_created[key]['tags']['Name']
            })
    return hosts

def generate_inventory(hosts, file_name='hosts'):
    # print(hosts['masters'])
    # print(hosts['workers'])
    f = open(file_name, "w")
    f.write("[masters]\n")
    for master in hosts['masters']:
        f.write('{tag} ansible_host={public_ip}\n'.format(tag=master['tag'], public_ip=master['public_ip']))
    f.write('\n\n')
    f.write("[workers]\n")
    for worker in hosts['workers']:
        f.write('{tag} ansible_host={public_ip}\n'.format(tag=worker['tag'], public_ip=worker['public_ip']))
    f.write('\n\n')

    f.write('[all:vars]\n')
    f.write('ansible_python_interpreter=/usr/bin/python3\n')
    f.write('ansible_user=admin\n')
    f.close()
    print('ansible inventory generated check /root/playbooks/output/hosts')

def main():
    hosts = extract_hosts()
    generate_inventory(hosts)

main()

# terraform output -json > output/terraform-output.json
# cd output && python3 generate_host.py
# mv /etc/ansible/hosts /etc/ansible/hosts_old
# cp hosts /etc/ansible/
