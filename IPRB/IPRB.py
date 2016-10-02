#Rosalind problem "Mendel's First Law"

k = int(raw_input("Please enter k: "))
m = int(raw_input("Please enter m: "))
n = int(raw_input("Please enter n: "))

total = k + m + n

hom_dom_both = (float(k)/total)*(float(k-1)/(total-1))*1

hom_dom_one_het =  (float(k)/total)*(float(m)/(total-1))*1
het_one_hom_dom =  (float(m)/total)*(float(k)/(total-1))*1

hom_dom_one_hom_rec = (float(k)/total)*(float(n)/(total-1))*1
hom_rec_one_hom_dom = (float(n)/total)*(float(k)/(total-1))*1

het_both = (float(m)/total)*(float(m-1)/(total-1))*(.75)

het_one_hom_rec = (float(m)/total)*(float(n)/(total-1))*(.5)
hom_rec_one_het = (float(n)/total)*(float(m)/(total-1))*(.5)

prob_tot = hom_dom_both + hom_dom_one_het + het_one_hom_dom + hom_dom_one_hom_rec + hom_rec_one_hom_dom + het_both + het_one_hom_rec + hom_rec_one_het

print prob_tot 