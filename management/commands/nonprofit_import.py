import os
import csv
from django.core.management.base import NoArgsCommand
from quarterback.irs.models import *

class Command(NoArgsCommand):
    help = "Download new files representing one month of 990s, ignoring months we already have"
    
    def handle_noargs(self, **options):
        
        existing_filenames = list(Nonprofit.objects.values_list('filename',flat=True).distinct())

        #download zip of all 990s, one file per month
        try:
            os.mkdir('/tmp/irs')
        except:
            pass
        os.system('wget https://bulk.resource.org/irs.gov/eo/manifests.tgz -O /tmp/irs/manifests.tgz')
        try:
            os.mkdir('/tmp/irs/extract')
        except:
            pass
        os.chdir('/tmp/irs/extract')
        os.system('gunzip -c /tmp/irs/manifests.tgz | tar -xvf -')


        #fout.writerow(['filename','doctype','year','url','id','name','formtype','date','size','assetts','hash','md5'])
        #manifest.2010_12_EO.txt,EO,90EZ,/irs.gov/eo/2010_12_EO/68-0142907_990EZ_200812.pdf,68-0142907,SKYLINE HARVEST INC,990EZ,12/2008,252 kB,0.00,96fd2051-50fc-11ed-0000-575aa217dde7,526b283d3d0c76540b9e9de16099523cde70659c724418b94ddf67a2e35b40b2

        for folder in os.listdir('.'):
            for filename in os.listdir(folder):
                if filename in existing_filenames:
                    print 'skipping %s, already have it' % filename
                    continue
                print 'importing %s' % filename
                objs = [] #bulk_insert 1000 at a time
                fin = open(os.path.join(folder,filename),'r')
                for line in fin:
                    (url,id,name,formtype,date,size,assets,hashstr,md5) = line.split('\t')
                    md5 = md5.strip()
                    assets = assets.replace(',','')
                    try:
                        assets = float(assets)
                    except:
                        assets = None
                    doctype = folder[-2:]
                    year = date[-4:]
                    d = {'url': url,'filename':filename,'doctype':doctype,'year':year,'idstr':id,'text':name,'formtype':formtype,'date':date,'size':size,'assetts':assets,'hashstr':hashstr,'md5':md5}
                    objs.append(Nonprofit(**d))
                    if len(objs)==1000:
                        Nonprofit.objects.bulk_create(objs)
                    objs = []
                Nonprofit.objects.bulk_create(objs)

