import os
def main():
    for x in range(11):
        makedb = "makeblastdb -in proteoom_"+str(int(x+1))+'.fasta -dbtype prot -title "db_proteoom_"'+str(int(x+1))
        os.system(makedb)
        print("Er is een database gemaakt van proteoom "+str(int(x+1))) 
        for y in range(11):
            if x == y:
                pass
            else:
                blast = 'blastp -db "proteoom_"'+str(int(x+1)) +'.fasta -query proteoom_'+str(int(y+1))+'.fasta -out db_proteoom_'+str(int(x+1))+'_tegen_proteoom_'+str(int(y+1))+'.out -outfmt "10"' 
                os.system(blast)
                print("proteoom "+str(int(y+1))+" is geblast tegen proteoom "+str(int(x+1)))
    print("Done")
                
main()
