import sys

f = open("c:\\temp\\checks_list.txt", "r")

orig_stdout = sys.stdout
z = open("c:\\temp\\out.txt", 'w')
sys.stdout = z


for x in f:
  print('define service    {')
  print('        use                              check-service-24x7_15min')
  print('        host_name                        s-l-zoo1.itella.net,s-l-zoo2.itella.net,s-l-zoo3.itella.net')
  print('        service_description              '+x.rstrip("\n"))
  print('        check_command                    check_nrpe2!'+x.rstrip("\n"))
  print('        servicegroups                    production-services,itellafi-production-services')
  print('        contacts                         sp-ops')
  print('}')
  print()

sys.stdout = orig_stdout
z.close()
f.close()