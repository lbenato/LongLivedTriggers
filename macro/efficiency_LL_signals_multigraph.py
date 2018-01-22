#! /usr/bin/env python

import os, multiprocessing
import copy
import math
from array import array
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory
from ROOT import TFile, TChain, TTree, TCut, TH1, TH1F, TH2F, THStack, TGraph, TGraphAsymmErrors, TSpline, TSpline3, TMultiGraph
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText, TLine, TBox


#from Analysis.ALPHA.LdrawUtils_thesis import *
#from Analysis.ALPHA.variables import *
#from Analysis.ALPHA.Lselections import *
#from Analysis.ALPHA.samples import sample, samples

LOCAL = False


if LOCAL:
    from samples import sample, samples
else:
    from LongLived.LongLivedTriggers.samples import sample, samples


########## SETTINGS ##########

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-v", "--variable", action="store", type="string", dest="variable", default="")
parser.add_option("-c", "--cut", action="store", type="string", dest="cut", default="")
parser.add_option("-r", "--region", action="store", type="string", dest="region", default="")
parser.add_option("-a", "--all", action="store_true", default=False, dest="all")
parser.add_option("-b", "--bash", action="store_true", default=False, dest="bash")
parser.add_option("-B", "--blind", action="store_true", default=False, dest="blind")
parser.add_option("-f", "--final", action="store_true", default=False, dest="final")
(options, args) = parser.parse_args()
if options.bash: gROOT.SetBatch(True)

########## SETTINGS ##########

gStyle.SetOptStat(0)

if LOCAL:
    NTUPLEDIR   = "/home/lisa/LongLived_local/LongLivedTriggers/crab_projects_LL_18jan/"
else:
    NTUPLEDIR   = "$CMSSW_BASE/src/LongLived/LongLivedTriggers/crab_projects_LL_18jan/"
#LUMI        = 36814 # in pb-1
SIGNAL      = 1.
RATIO       = 4 # 0: No ratio plot; !=0: ratio between the top and bottom pads
BLIND       = False
POISSON     = False
jobs        = []

########## SAMPLES ##########

#sign = ["XZZ_M600", "XZZ_M650", "XZZ_M700", "XZZ_M750", "XZZ_M800", "XZZ_M1000", "XZZ_M1200", "XZZ_M1400", "XZZ_M1800", "XZZ_M2000", "XZZ_M2500", "XZZ_M3000", "XZZ_M3500", "XZZ_M4000", "XZZ_M4500"]
### WprimeToWZToWhadZlep
#sign = ["XWZ_M600", "XWZ_M800", "XWZ_M1000", "XWZ_M1200", "XWZ_M1400", "XWZ_M1600", "XWZ_M1800", "XWZ_M2000", "XWZ_M2500", "XWZ_M3000", "XWZ_M3500", "XWZ_M4000", "XWZ_M4500"]
#ZhadZinv
#sign = ["XZZInv_M600", "XZZInv_M800", "XZZInv_M1000", "XZZInv_M1200", "XZZInv_M1400", "XZZInv_M1600", "XZZInv_M1800", "XZZInv_M2000", "XZZInv_M2500", "XZZInv_M3000", "XZZInv_M3500", "XZZInv_M4000", "XZZInv_M4500"]#"XZZInv_M4000", 
#sign = ["XWZInv_M600", "XWZInv_M800", "XWZInv_M1000", "XWZInv_M1200", "XWZInv_M1400", "XWZInv_M1600", "XWZInv_M1800", "XWZInv_M2000", "XWZInv_M2500", "XWZInv_M3000", "XWZInv_M3500", "XWZInv_M4000", "XWZInv_M4500"]#"XZZInv_M4000", 
#sign_mass = ['WplusH_M15_ctau1000', 'WplusH_M40_ctau1000', 'WplusH_M55_ctau1000']
#sign_mass = ['WplusH_M15_ctau1', 'WplusH_M40_ctau1', 'WplusH_M55_ctau1']
sign_mass = ['WplusH_M15_ctau100', 'WplusH_M40_ctau100', 'WplusH_M55_ctau100']
sign_ctau = ['WplusH_M55_ctau0','WplusH_M55_ctau0p05','WplusH_M55_ctau1','WplusH_M55_ctau10','WplusH_M55_ctau100','WplusH_M55_ctau1000','WplusH_M55_ctau10000']#

#sign_mass = ['WminusH_M15_ctau10000','WminusH_M40_ctau10000','WminusH_M55_ctau10000']
#sign_ctau = ['WminusH_M15_ctau0','WminusH_M15_ctau0p05','WminusH_M15_ctau1','WminusH_M15_ctau10','WminusH_M15_ctau100','WminusH_M15_ctau1000','WminusH_M15_ctau10000']# 
#
#sign_mass = ['ZH_M15_ctau1000','ZH_M40_ctau1000','ZH_M55_ctau1000']
#sign_ctau = ['ZH_M15_ctau0','ZH_M15_ctau0p05','ZH_M15_ctau1','ZH_M15_ctau10','ZH_M15_ctau100','ZH_M15_ctau1000','ZH_M15_ctau10000']# 
#
#sign_mass = ['ggZH_M15_ctau1000','ggZH_M40_ctau1000','ggZH_M55_ctau1000']
#sign_ctau = ['ggZH_M15_ctau0','ggZH_M15_ctau0p05','ggZH_M15_ctau10','ggZH_M15_ctau100','ggZH_M15_ctau1000','ggZH_M15_ctau10000']# 

#sign = ["XZZInv_M600", "XZZInv_M1000", "XZZInv_M2000", "XZZInv_M3000", "XZZInv_M4000"]
colors = [4, 410, 856, 2, 634, 1, 881, 798, 602, 921, 801, 3, 5, 6, ]
########## ######## ##########

gROOT.SetBatch(True)




def efficiency(cutlist, labellist, setcut='',maxy=0.50, var=""):

    basecut = ""
    signame = ""
    ncuts = len(cutlist)
    
    file = {}
    nevt = {}
    tree = {}
    effs = {}

    if var=="mass":
        sign = sign_mass
        lab = ", c#tau = "#+samples[s]['ctau']+" (mm)"
    elif var=="ctau":
        sign = sign_ctau
        lab = ", m_{#pi} = "#+samples[s]['mass']+" (GeV)"

    for i, s in enumerate(sign):
        if 'WplusH' in samples[s]['files'][0]:
            signame = "WplusH"
        elif 'WminusH' in samples[s]['files'][0]:
            signame = "WminusH"
        elif 'ZH' in samples[s]['files'][0] and not 'ggZH' in samples[s]['files'][0]:
            signame = "ZH"
        elif 'ggZH' in samples[s]['files'][0]:
            signame = "ggZH"
        file[s] = TFile(NTUPLEDIR + samples[s]['files'][0] + ".root", "READ") # Read TFile
        ##nevt[s] = (file[s].Get('counter/c_nEvents')).GetBinContent(1)
        tree[s] = file[s].Get("trigger/tree") # Read TTree
        nevt[s] = file[s].Get("trigger/tree").GetEntriesFast()
        effs[s] = [0]*(ncuts+1)
        for j, c in enumerate(cutlist):
            br = 1.
            n = tree[s].GetEntries(cutlist[j])
            d = nevt[s]#d = sample[samples[s]['files'][0]]['nevents']#tree[s].GetEntries(basecut)
            effs[s][j] = float(n)/(d*br)
    
    if var=="mass":
        lab += str(samples[sign[0]]['ctau'])+" mm"
    elif var=="ctau":
        lab += str(samples[sign[0]]['mass'])+" GeV"
    mg = TMultiGraph("mg","")
    leg = TLegend(0.2, 0.6, 0.9, 0.9)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0) #1001
    leg.SetFillColor(0)
    for j, c in enumerate(cutlist):
        gr = TGraph(len(sign))
        for i, s in enumerate(sign):
            val_var = int(samples[s][var])
            #print i, mass, effs[s][j]
            gr.SetPoint(i, val_var, effs[s][j])
        gr.SetMarkerStyle(20)
        gr.SetMarkerColor(colors[j])
        gr.SetLineColor(colors[j])
        gr.SetLineWidth(3)
        gr.GetXaxis().SetTitleOffset(gr.GetXaxis().GetTitleOffset()*1.2)
        gr.GetYaxis().SetTitleOffset(gr.GetYaxis().GetTitleOffset()*1.2)
        if var=="mass":
            gr.GetXaxis().SetTitle("m_{#pi} (GeV)")
        elif var=="ctau":
            gr.GetXaxis().SetTitle("c#tau (mm)")
            #gr.GetXaxis().SetRangeUser(1, 100)
            #gr.GetXaxis().SetLimits(1,100)
        gr.GetYaxis().SetTitle("Efficiency")
        gr.GetYaxis().SetRangeUser(0., maxy)
        mg.Add(gr)
        leg.AddEntry(gr, labellist[j], "lp")
        
    if 'WplusH' in samples[s]['files'][0]:
        #leg.AddEntry(gr, 'W^{+} H #rightarrow #pi #pi #rightarrow 4b', "")
        leg.SetHeader('W^{+} H #rightarrow #pi #pi #rightarrow 4b'+lab, "")
    elif 'WminusH' in samples[s]['files'][0]:
        #leg.AddEntry(gr, 'W^{-} H #rightarrow #pi #pi #rightarrow 4b', "")
        leg.SetHeader('W^{-} H #rightarrow #pi #pi #rightarrow 4b'+lab, "")
    elif 'ZH' in samples[s]['files'][0] and not 'ggZH' in samples[s]['files'][0]:
        #leg.AddEntry(gr, 'Z H #rightarrow #pi #pi #rightarrow 4b', "")
        leg.SetHeader('Z H #rightarrow #pi #pi #rightarrow 4b'+lab, "")
    elif 'ggZH' in samples[s]['files'][0]:
        #leg.AddEntry(gr, 'gg Z H #rightarrow #pi #pi #rightarrow 4b', "")
        leg.SetHeader('gg Z H #rightarrow #pi #pi #rightarrow 4b'+lab, "")

    c1 = TCanvas("c1", "Signals", 800, 600)
    c1.cd()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)

    mg.Draw("APL")
    if var=="mass":
        mg.GetXaxis().SetTitle("m_{#pi} (GeV)")
    elif var=="ctau":
        mg.GetXaxis().SetTitle("c#tau (mm)")
    mg.GetYaxis().SetTitle("Efficiency")
    mg.GetYaxis().SetRangeUser(0., maxy)
    #if var=="ctau":
        #c1.SetLogx()
        #mg.GetXaxis().SetRangeUser(1, 100)#20000)
        #mg.Draw("APL")
        #mg.GetXaxis().SetLimits(1,100)
        #mg.Draw("APL")
    leg.Draw()
    #drawCMS(-1, "Simulation")
        
    c1.Print("$CMSSW_BASE/src/LongLived/LongLivedTriggers/macro/Efficiency/Efficiency_vs_" +str(var)+"_" + signame + setcut+".png")
    c1.Print("$CMSSW_BASE/src/LongLived/LongLivedTriggers/macro/Efficiency/Efficiency_vs_" +str(var)+"_" + signame + setcut+".pdf")
    #if not options.runBash: raw_input("Press Enter to continue...")
    c1.Close()




###################

'''def efficiency_mass(cutlist, labellist, setcut='',maxy=0.50):

    basecut = ""
    signame = ""
    ncuts = len(cutlist)
    
    file = {}
    nevt = {}
    tree = {}
    effs = {}

    for i, s in enumerate(sign_mass):
        if 'WplusH' in samples[s]['files'][0]:
            signame = "WplusH"
        elif 'WminusH' in samples[s]['files'][0]:
            signame = "WminusH"
        elif 'ZH' in samples[s]['files'][0] and not 'ggZH' in samples[s]['files'][0]:
            signame = "ZH"
        elif 'ggZH' in samples[s]['files'][0]:
            signame = "ggZH"
        file[s] = TFile(NTUPLEDIR + samples[s]['files'][0] + ".root", "READ") # Read TFile
        ##nevt[s] = (file[s].Get('counter/c_nEvents')).GetBinContent(1)
        tree[s] = file[s].Get("trigger/tree") # Read TTree
        nevt[s] = file[s].Get("trigger/tree").GetEntriesFast()
        effs[s] = [0]*(ncuts+1)
        for j, c in enumerate(cutlist):
            br = 1.
            n = tree[s].GetEntries(cutlist[j])
            d = nevt[s]#d = sample[samples[s]['files'][0]]['nevents']#tree[s].GetEntries(basecut)
            effs[s][j] = float(n)/(d*br)
    
    mg = TMultiGraph("mg","")
    leg = TLegend(0.2, 0.6, 0.9, 0.9)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0) #1001
    leg.SetFillColor(0)
    for j, c in enumerate(cutlist):
        gr = TGraph(len(sign_mass))
        for i, s in enumerate(sign_mass):
            mass = int(samples[s]['mass'])
            #print i, mass, effs[s][j]
            gr.SetPoint(i, mass, effs[s][j])
        gr.SetMarkerStyle(20)
        gr.SetMarkerColor(colors[j])
        gr.SetLineColor(colors[j])
        gr.SetLineWidth(3)
        gr.GetXaxis().SetTitleOffset(gr.GetXaxis().GetTitleOffset()*1.2)
        gr.GetYaxis().SetTitleOffset(gr.GetYaxis().GetTitleOffset()*1.2)
        gr.GetXaxis().SetTitle("m_{#pi} (GeV)")
        gr.GetYaxis().SetTitle("Efficiency")
        gr.GetYaxis().SetRangeUser(0., maxy)
        mg.Add(gr)
        leg.AddEntry(gr, labellist[i], "lp")
        
    if 'WplusH' in samples[s]['files'][0]:
        #leg.AddEntry(gr, 'W^{+} H #rightarrow #pi #pi #rightarrow 4b', "")
        leg.SetHeader('W^{+} H #rightarrow #pi #pi #rightarrow 4b', "")
    elif 'WminusH' in samples[s]['files'][0]:
        #leg.AddEntry(gr, 'W^{-} H #rightarrow #pi #pi #rightarrow 4b', "")
        leg.SetHeader('W^{-} H #rightarrow #pi #pi #rightarrow 4b', "")
    elif 'ZH' in samples[s]['files'][0] and not 'ggZH' in samples[s]['files'][0]:
        #leg.AddEntry(gr, 'Z H #rightarrow #pi #pi #rightarrow 4b', "")
        leg.SetHeader('Z H #rightarrow #pi #pi #rightarrow 4b', "")
    elif 'ggZH' in samples[s]['files'][0]:
        #leg.AddEntry(gr, 'gg Z H #rightarrow #pi #pi #rightarrow 4b', "")
        leg.SetHeader('gg Z H #rightarrow #pi #pi #rightarrow 4b', "")

    c1 = TCanvas("c1", "Signals", 800, 600)
    c1.cd()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)

    mg.Draw("APL")
    mg.GetXaxis().SetTitle("m_{#pi} (GeV)")
    mg.GetYaxis().SetTitle("Efficiency")
    mg.GetYaxis().SetRangeUser(0., maxy)
    leg.Draw()
    #drawCMS(-1, "Simulation")
        
    c1.Print("$CMSSW_BASE/src/LongLived/LongLivedTriggers/macro/Efficiency/Efficiency_vs_mass_" + signame + setcut+"_mg.png")
    c1.Print("$CMSSW_BASE/src/LongLived/LongLivedTriggers/macro/Efficiency/Efficiency_vs_mass_" + signame + setcut+"_mg.pdf")
    #if not options.runBash: raw_input("Press Enter to continue...")

def efficiency_ctau_new(cutlist, labellist, setcut='',maxy=0.50):

    basecut = ""
    signame = ""
    ncuts = len(cutlist)
    
    file = {}
    nevt = {}
    tree = {}
    effs = {}

    for i, s in enumerate(sign_ctau):
        if 'WplusH' in samples[s]['files'][0]:
            signame = "WplusH"
        elif 'WminusH' in samples[s]['files'][0]:
            signame = "WminusH"
        elif 'ZH' in samples[s]['files'][0] and not 'ggZH' in samples[s]['files'][0]:
            signame = "ZH"
        elif 'ggZH' in samples[s]['files'][0]:
            signame = "ggZH"
        file[s] = TFile(NTUPLEDIR + samples[s]['files'][0] + ".root", "READ") # Read TFile
        ##nevt[s] = (file[s].Get('counter/c_nEvents')).GetBinContent(1)
        tree[s] = file[s].Get("trigger/tree") # Read TTree
        nevt[s] = file[s].Get("trigger/tree").GetEntriesFast()
        effs[s] = [0]*(ncuts+1)
        for j, c in enumerate(cutlist):
            br = 1.
            n = tree[s].GetEntries(cutlist[j])
            d = nevt[s]#d = sample[samples[s]['files'][0]]['nevents']#tree[s].GetEntries(basecut)
            effs[s][j] = float(n)/(d*br)
    
    mg2 = TMultiGraph("mg2","")
    leg2 = TLegend(0.2, 0.6, 0.9, 0.9)
    leg2.SetBorderSize(0)
    leg2.SetFillStyle(0) #1001
    leg2.SetFillColor(0)
    for j, c in enumerate(cutlist):
        gr = TGraph(len(sign_ctau))
        for i, s in enumerate(sign_ctau):
            ctau = int(samples[s]['ctau'])
            #print i, ctau, effs[s][j]
            gr.SetPoint(i, ctau, effs[s][j])
        gr.SetMarkerStyle(20)
        gr.SetMarkerColor(colors[j])
        gr.SetLineColor(colors[j])
        gr.SetLineWidth(3)
        gr.GetXaxis().SetTitleOffset(gr.GetXaxis().GetTitleOffset()*1.2)
        gr.GetYaxis().SetTitleOffset(gr.GetYaxis().GetTitleOffset()*1.2)
        gr.GetXaxis().SetTitle("m_{#pi} (GeV)")
        gr.GetYaxis().SetTitle("Efficiency")
        gr.GetYaxis().SetRangeUser(0., maxy)
        mg2.Add(gr)
        leg2.AddEntry(gr, labellist[i], "lp")
        
    if 'WplusH' in samples[s]['files'][0]:
        #leg.AddEntry(gr, 'W^{+} H #rightarrow #pi #pi #rightarrow 4b', "")
        leg2.SetHeader('W^{+} H #rightarrow #pi #pi #rightarrow 4b', "")
    elif 'WminusH' in samples[s]['files'][0]:
        #leg.AddEntry(gr, 'W^{-} H #rightarrow #pi #pi #rightarrow 4b', "")
        leg2.SetHeader('W^{-} H #rightarrow #pi #pi #rightarrow 4b', "")
    elif 'ZH' in samples[s]['files'][0] and not 'ggZH' in samples[s]['files'][0]:
        #leg.AddEntry(gr, 'Z H #rightarrow #pi #pi #rightarrow 4b', "")
        leg2.SetHeader('Z H #rightarrow #pi #pi #rightarrow 4b', "")
    elif 'ggZH' in samples[s]['files'][0]:
        #leg.AddEntry(gr, 'gg Z H #rightarrow #pi #pi #rightarrow 4b', "")
        leg2.SetHeader('gg Z H #rightarrow #pi #pi #rightarrow 4b', "")

    c1 = TCanvas("c1", "Signals", 800, 600)
    c1.cd()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)

    mg2.Draw("APL")
    mg2.GetXaxis().SetTitle("m_{#pi} (GeV)")
    mg2.GetYaxis().SetTitle("Efficiency")
    mg2.GetYaxis().SetRangeUser(0., maxy)
    leg2.Draw()
    #drawCMS(-1, "Simulation")
        
    c1.Print("$CMSSW_BASE/src/LongLived/LongLivedTriggers/macro/Efficiency/Efficiency_vs_ctau_" + signame + setcut+"_mg.png")
    c1.Print("$CMSSW_BASE/src/LongLived/LongLivedTriggers/macro/Efficiency/Efficiency_vs_ctau_" + signame + setcut+"_mg.pdf")
    #if not options.runBash: raw_input("Press Enter to continue...")



def efficiency_ctau(cutlist, labellist, setcut='',maxy=0.50):

    basecut = ""
    signame = ""
    ncuts = len(cutlist)
    
    file = {}
    nevt = {}
    tree = {}
    effs = {}

    for i, s in enumerate(sign_ctau):
        print "c_tau sample: ", s
        if 'BulkGravToZZToZhadZinv' in samples[s]['files'][0]:
            signame = "XZZInv"
        elif 'WprimeToWZToWhadZinv' in samples[s]['files'][0]:
            signame = "XWZInv"
        elif 'WplusH' in samples[s]['files'][0]:
            signame = "WplusH"
        elif 'WminusH' in samples[s]['files'][0]:
            signame = "WminusH"
        elif 'ZH' in samples[s]['files'][0] and not 'ggZH' in samples[s]['files'][0]:
            signame = "ZH"
        elif 'ggZH' in samples[s]['files'][0]:
            signame = "ggZH"
        file[s] = TFile(NTUPLEDIR + samples[s]['files'][0] + ".root", "READ") # Read TFile
        ##nevt[s] = (file[s].Get('counter/c_nEvents')).GetBinContent(1)
        tree[s] = file[s].Get("trigger/tree") # Read TTree
        nevt[s] = file[s].Get("trigger/tree").GetEntriesFast()
        effs[s] = [0]*(ncuts+1)
        for j, c in enumerate(cutlist):
            #print cutlist[j]

            br = 1.
            n = tree[s].GetEntries(cutlist[j])
            d = nevt[s]#d = sample[samples[s]['files'][0]]['nevents']#tree[s].GetEntries(basecut)
            effs[s][j] = float(n)/(d*br)
    
    line_ctau = []
    outFile = TFile("$CMSSW_BASE/src/LongLived/LongLivedTriggers/macro/Efficiency/Eff_spline.root", "UPDATE")
    outFile.cd()
    #flagLP = True
    for j, c in enumerate(cutlist):
        line_ctau.append( TGraph(ncuts) )
        line_ctau[j].SetTitle(";c#tau_{#pi} (mm);Efficiency")
        #print labellist[j]
        for i, s in enumerate(sign_ctau):
            #mass = int( ''.join(x for x in s if x.isdigit()) )
            ctau = float(samples[s]['ctau'])
            #print i, ctau, effs[s][j]
            line_ctau[j].SetPoint(i, ctau, effs[s][j])
        line_ctau[j].SetMarkerStyle(20)
        line_ctau[j].SetMarkerColor(colors[j])
        line_ctau[j].SetLineColor(colors[j])
        line_ctau[j].SetLineWidth(3)
        line_ctau[j].GetXaxis().SetTitleOffset(line_ctau[j].GetXaxis().GetTitleOffset()*1.2)
        line_ctau[j].GetYaxis().SetTitleOffset(line_ctau[j].GetYaxis().GetTitleOffset()*1.2)
        #line_ctau[j].Print()
        
    outFile.Close()
    leg = TLegend(0.2, 0.6, 0.9, 0.9)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0) #1001
    leg.SetFillColor(0)
    for i, c in enumerate(cutlist):
        leg.AddEntry(line_ctau[i], labellist[i], "lp")

    if 'BulkGravToZZToZlepZhad' in samples[s]['files'][0]:
        leg.AddEntry(line_ctau[0], 'G_{Bulk} #rightarrow Z_{had}Z_{lep}', "")
    elif 'BulkGravToZZToZlepZinv' in samples[s]['files'][0]:
        leg.AddEntry(line_ctau[0], 'G_{Bulk} #rightarrow Z_{lep}Z_{inv}', "")
    elif 'WprimeToWZToWhadZlep' in samples[s]['files'][0]:
        leg.AddEntry(line_ctau[0], 'W\' #rightarrow W_{had}Z_{lep}', "")
    elif 'BulkGravToZZToZhadZinv' in samples[s]['files'][0]:
        #signame += "XZZInv"
        leg.AddEntry(line_ctau[0], 'G_{Bulk} #rightarrow Z_{had}Z_{inv}', "")
    elif 'WprimeToWZToWhadZinv' in samples[s]['files'][0]:
        #signame += "XWZInv"
        leg.AddEntry(line_ctau[0], 'W\' #rightarrow W_{had}Z_{inv}', "")
    elif 'WplusH' in samples[s]['files'][0]:
        #signame += "XWZInv"
        leg.AddEntry(line_ctau[0], 'W^{+} H #rightarrow #pi #pi #rightarrow 4b', "")
    elif 'WminusH' in samples[s]['files'][0]:
        leg.AddEntry(line_ctau[0], 'W^{-} H #rightarrow #pi #pi #rightarrow 4b', "")
    elif 'ZH' in samples[s]['files'][0] and not 'ggZH' in samples[s]['files'][0]:
        leg.AddEntry(line_ctau[0], 'Z H #rightarrow #pi #pi #rightarrow 4b', "")
    elif 'ggZH' in samples[s]['files'][0]:
        leg.AddEntry(line_ctau[0], 'gg Z H #rightarrow #pi #pi #rightarrow 4b', "")
    
    c1 = TCanvas("c1", "Signals", 800, 600)
    c1.cd()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)
    line_ctau[0].GetXaxis().SetTitle("c#tau_{#pi} (mm)")
    line_ctau[0].GetYaxis().SetTitle("Efficiency")
    line_ctau[0].GetYaxis().SetRangeUser(0., maxy)
    
    for i, s in enumerate(cutlist):
        line_ctau[i].Draw("APL" if i==0 else "SAME, PL")
    leg.Draw()
    #drawCMS(-1, "Simulation")
    
    name = ""
    if '#mu#mu' in labellist[0]: name = "Muon"
    elif 'ee' in labellist[0]: name = "Ele"
    else: name = "Met"
    
    c1.Print("$CMSSW_BASE/src/LongLived/LongLivedTriggers/macro/Efficiency/Efficiency_vs_ctau_" + signame + setcut+"_mg.png")
    c1.Print("$CMSSW_BASE/src/LongLived/LongLivedTriggers/macro/Efficiency/Efficiency_vs_ctau_" + signame + setcut+"_mg.pdf")
    #c1.Print("$CMSSW_BASE/src/LongLived/LongLivedTriggers/macro/Efficiency/Efficiency_vs_ctau_" + signame + setcut+".C")
    line_ctau = []
'''




'''efficiency_mass([
    'HLT_CaloJet260_v', 
    'HLT_CaloJet500_NoJetID_v',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v',
    'HLT_HT250_CaloMET70_v',
    'HLT_PFJet450_v || HLT_HT650_v',
#    'HLT_PFJet15_NoCaloMatched_v',#weird, check
    ],
    [
    'HLT_CaloJet260_v', 
    'HLT_CaloJet500_NoJetID_v',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v',
    'HLT_HT250_CaloMET70_v',
    'HLT_PFJet450_v || HLT_HT650_v',
#    'HLT_PFJet15_NoCaloMatched_v',#weird, check
    ],
"calo"
)


efficiency_mass([
#    'isMC',
    'HLT_IsoMu24_v || HLT_IsoTkMu24_v',
    'HLT_Ele27_WPTight_Gsf_v',
    #'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v',
    'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v',
    'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v',
    'HLT_Mu3_PFJet40_v',
],
    [
#    'is MC',
    'HLT_IsoMu24_v || HLT_IsoTkMu24_v',
    'HLT_Ele27_WPTight_Gsf_v',
    #'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v',
    'HLT Ele8_CaloIdM_TrackIdM_PFJet30_v',
    'HLT Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v',
    'HLT_Mu3_PFJet40_v',
    ],
 "lept"
)

efficiency_mass([
    'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v',
    'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v',
    'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v',
    'HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v',
    'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v',
    'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
],
    [
    'HLT HT350_DisplacedDijet80_Tight_DisplacedTrack_v',
    'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v',
    'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v',
    'HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v',
    'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v',
    'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
    ],
"displ"
)

efficiency_mass([
    'HLT_IsoMu24_v || HLT_IsoTkMu24_v || HLT_Ele27_WPTight_Gsf_v',
    'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v || HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v || HLT_Mu3_PFJet40_v || HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v',
    'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v || HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v || HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v || HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
    'HLT_CaloJet260_v || HLT_CaloJet500_NoJetID_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v || HLT_HT250_CaloMET70_v || HLT_PFJet450_v || HLT_HT650_v',
    'HLT_IsoMu24_v || HLT_IsoTkMu24_v || HLT_Ele27_WPTight_Gsf_v || HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v || HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v || HLT_Mu3_PFJet40_v || HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v || HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v || HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v || HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v || HLT_Ele27_WPLoose_Gsf_WHbbBoost_v || HLT_CaloJet260_v || HLT_CaloJet500_NoJetID_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v || HLT_HT250_CaloMET70_v || HLT_PFJet450_v || HLT_HT650_v',
],
    [
#    'is MC',
    'SingleEle || Single Mu',
    'Ele + jet (HT) || Mu + jet',
    'Displacement + boost WHbb',
    'Calo + PF/HT',
    'OR',
    ],
    "OR",
    0.8
)

#raw_input('pausa')

    

efficiency_ctau([
    'HLT_CaloJet260_v', 
    'HLT_CaloJet500_NoJetID_v',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v',
    'HLT_HT250_CaloMET70_v',
    'HLT_PFJet450_v || HLT_HT650_v',
#    'HLT_PFJet15_NoCaloMatched_v',#weird, check
    ],
    [
    'HLT_CaloJet260_v', 
    'HLT_CaloJet500_NoJetID_v',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v',
    'HLT_HT250_CaloMET70_v',
    'HLT_PFJet450_v || HLT_HT650_v',
#    'HLT_PFJet15_NoCaloMatched_v',#weird, check
    ],
"calo"
)

efficiency_ctau([
#    'isMC',
    'HLT_IsoMu24_v || HLT_IsoTkMu24_v',
    'HLT_Ele27_WPTight_Gsf_v',
    #'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v',
    'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v',
    'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v',
    'HLT_Mu3_PFJet40_v',
],
    [
#    'is MC',
    'HLT_IsoMu24_v || HLT_IsoTkMu24_v',
    'HLT_Ele27_WPTight_Gsf_v',
    #'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v',
    'HLT Ele8_CaloIdM_TrackIdM_PFJet30_v',
    'HLT Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v',
    'HLT_Mu3_PFJet40_v',
    ],
 "lept"
)

efficiency_ctau([
    'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v',
    'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v',
    'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v',
    'HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v',
    'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v',
    'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
],
    [
    'HLT HT350_DisplacedDijet80_Tight_DisplacedTrack_v',
    'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v',
    'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v',
    'HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v',
    'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v',
    'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
    ],
"displ"
)

efficiency_ctau([
#    'isMC',
    'HLT_IsoMu24_v || HLT_IsoTkMu24_v || HLT_Ele27_WPTight_Gsf_v',
    'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v || HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v || HLT_Mu3_PFJet40_v || HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v',
    'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v || HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v || HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v || HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
    'HLT_CaloJet260_v || HLT_CaloJet500_NoJetID_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v || HLT_HT250_CaloMET70_v || HLT_PFJet450_v || HLT_HT650_v',
    'HLT_IsoMu24_v || HLT_IsoTkMu24_v || HLT_Ele27_WPTight_Gsf_v || HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v || HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v || HLT_Mu3_PFJet40_v || HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v || HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v || HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v || HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v || HLT_Ele27_WPLoose_Gsf_WHbbBoost_v || HLT_CaloJet260_v || HLT_CaloJet500_NoJetID_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v || HLT_HT250_CaloMET70_v || HLT_PFJet450_v || HLT_HT650_v',
],
    [
#    'is MC',
    'SingleEle || Single Mu',
    'Ele + jet (HT) || Mu + jet',
    'Displacement + boost WHbb',
    'Calo + PF/HT',
    'OR',
    ],
    "OR",
    1.0            
)'''


'''efficiency([
    'HLT_CaloJet260_v', 
    'HLT_CaloJet500_NoJetID_v',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v',
    'HLT_HT250_CaloMET70_v',
    'HLT_PFJet450_v || HLT_HT650_v',
#    'HLT_PFJet15_NoCaloMatched_v',#weird, check
    ],
    [
    'HLT_CaloJet260_v', 
    'HLT_CaloJet500_NoJetID_v',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v',
    'HLT_HT250_CaloMET70_v',
    'HLT_PFJet450_v || HLT_HT650_v',
#    'HLT_PFJet15_NoCaloMatched_v',#weird, check
    ],
"lept",
0.5,
"ctau"
)'''

for a in ['mass','ctau']:

    efficiency([
            'HLT_CaloJet260_v', 
            'HLT_CaloJet500_NoJetID_v',
            'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v',
            'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v',
            'HLT_HT250_CaloMET70_v',
            'HLT_PFJet450_v || HLT_HT650_v',
#    'HLT_PFJet15_NoCaloMatched_v',#weird, check
            ],
                    [
            'HLT_CaloJet260_v', 
            'HLT_CaloJet500_NoJetID_v',
            'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v',
            'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v',
            'HLT_HT250_CaloMET70_v',
            'HLT_PFJet450_v || HLT_HT650_v',
#    'HLT_PFJet15_NoCaloMatched_v',#weird, check
            ],
               "calo",
               0.5,
               a
               )

    efficiency([
#    'isMC',
            'HLT_IsoMu24_v || HLT_IsoTkMu24_v',
            'HLT_Ele27_WPTight_Gsf_v',
    #'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
            'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v',
            'HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v',
            'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v',
            'HLT_Mu3_PFJet40_v',
            ],
               [
#    'is MC',
            'HLT_IsoMu24_v || HLT_IsoTkMu24_v',
            'HLT_Ele27_WPTight_Gsf_v',
    #'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
            'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v',
            'HLT Ele8_CaloIdM_TrackIdM_PFJet30_v',
            'HLT Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v',
            'HLT_Mu3_PFJet40_v',
            ],
               "lept",
               0.5,
               a
               )


    efficiency([
            'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v',
            'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v',
            'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v',
            'HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v',
            'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v',
            'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
            ],
               [
            'HLT HT350_DisplacedDijet80_Tight_DisplacedTrack_v',
            'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v',
            'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v',
            'HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v',
            'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v',
            'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
            ],
               "displ",
               0.5,
               a
               )


    efficiency([
            'HLT_IsoMu24_v || HLT_IsoTkMu24_v || HLT_Ele27_WPTight_Gsf_v',
            'HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v || HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v || HLT_Mu3_PFJet40_v || HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v',
            'HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v || HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v || HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v || HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',
            'HLT_CaloJet260_v || HLT_CaloJet500_NoJetID_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v || HLT_HT250_CaloMET70_v || HLT_PFJet450_v || HLT_HT650_v',
            'HLT_IsoMu24_v || HLT_IsoTkMu24_v || HLT_Ele27_WPTight_Gsf_v || HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v || HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v || HLT_Mu3_PFJet40_v || HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v || HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v || HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v || HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v || HLT_Ele27_WPLoose_Gsf_WHbbBoost_v || HLT_CaloJet260_v || HLT_CaloJet500_NoJetID_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v || HLT_HT250_CaloMET70_v || HLT_PFJet450_v || HLT_HT650_v',
            ],
               [
#    'is MC',
            'SingleEle || Single Mu',
            'Ele + jet (HT) || Mu + jet',
            'Displacement + boost WHbb',
            'Calo + PF/HT',
            'OR',
            ],
               "OR",
               0.8,
               a
               )

