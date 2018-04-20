#! /usr/bin/env python

#voms-proxy-init -voms cms
#

#Higgs production cross sections: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHXSWG#Production_cross_sections_and_de
    #ggH xsec: 48.58
    #VBF xsec: 3.782
    #WH xsec: 1.373
    #ZH xsec: 0.8839

sample = {
    ########## DATA ##########

    ### Signal ###
    #WplusH_HToSSTobbbb_WToLNu
    #m = 15 GeV
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    #m = 40 GeV
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    #m = 55 GeV
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*10.86,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    #ZH_HToSSTobbbb_WToLNu
    #m = 15 GeV
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    #m = 40 GeV
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    #m = 55 GeV
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    #ggZH_HToSSTobbbb_WToLNu
    #m = 15 GeV
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    #m = 40 GeV
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    #m = 55 GeV
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.*3.3658,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
#VBF
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0p05_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0p1_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-1_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-10_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-25_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-50_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-100_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-500_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-1000_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-2000_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5000_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-10000_Summer16_MINIAOD' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

#VBF true higgs
    'VBFHToBB_M-125_13TeV_powheg_pythia8' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    
}





samples = {
    'data_obs' : {
        'order' : 0,
        'files' : ['METRun2016B-03Feb2017_ver2-v2', 'METRun2016C-03Feb2017-v1', 'METRun2016D-03Feb2017-v1', 'METRun2016E-03Feb2017-v1', 'METRun2016F-03Feb2017-v1', 'METRun2016G-03Feb2017-v1', 'METRun2016H-03Feb2017_ver2-v1', 'METRun2016H-03Feb2017_ver3-v1'],
 #       'files' : ['METRun2016H-03Feb2017_ver3-v1'],
 #        'files' : ['METRun2016B-23Sep2016-v2', 'METRun2016B-23Sep2016-v3', 'METRun2016C-23Sep2016-v1', 'METRun2016D-23Sep2016-v1', 'METRun2016E-23Sep2016-v1', 'METRun2016F-23Sep2016-v1', 'METRun2016G-23Sep2016-v1', 'METRun2016H-PromptReco-v1', 'METRun2016H-PromptReco-v2', 'METRun2016H-PromptReco-v3'],
        'fillcolor' : 0,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Data",
        'weight': 1.,
        'plot': True,
    },
    # Dummy entry for background sum
    'BkgSum' : {
        'order' : 0,
        'files' : [],
        'fillcolor' : 1,
        'fillstyle' : 3003,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Bkg stat.",
        'weight': 1.,
        'plot': True,
    },
    

    #WplusH PiPi
    'WplusH_M15_ctau0' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 0.,
    },
    'WplusH_M15_ctau0p05' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 0.05,
    },
    'WplusH_M15_ctau1' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 1,
    },
    'WplusH_M15_ctau10' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 10,
    },
    'WplusH_M15_ctau100' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 100,
    },
    'WplusH_M15_ctau1000' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 1000,
    },

    'WplusH_M40_ctau0' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 0,
    },
    'WplusH_M40_ctau0p05' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 0.05,
    },
    'WplusH_M40_ctau1' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 1,
    },
    'WplusH_M40_ctau10' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 10,
    },
    'WplusH_M40_ctau100' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 100,
    },
    'WplusH_M40_ctau1000' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 1000,
    },

    'WplusH_M55_ctau0' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 0,
    },
    'WplusH_M55_ctau0p05' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 0.05,
    },

    'WplusH_M55_ctau1' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 1,
    },
    'WplusH_M55_ctau10' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 10,
    },
    'WplusH_M55_ctau100' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 100,
    },
    'WplusH_M55_ctau1000' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 1000,
    },
    'WplusH_M55_ctau10000' : {
        'files' : ['WplusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 10000,
    },

    #WminusH Pi Pi
    'WminusH_M15_ctau0' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 0,
    },
    'WminusH_M15_ctau0p05' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 0.05,
    },
    'WminusH_M15_ctau1' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 1,
    },
    'WminusH_M15_ctau10' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 10,
    },
    'WminusH_M15_ctau100' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 100,
    },
    'WminusH_M15_ctau1000' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 1000,
    },
    'WminusH_M15_ctau10000' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 10000,
    },

    'WminusH_M40_ctau0' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 0,
    },
    'WminusH_M40_ctau0p05' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 0.05,
    },
    'WminusH_M40_ctau1' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 1,
    },
    'WminusH_M40_ctau10' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 10,
    },
    'WminusH_M40_ctau100' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 100,
    },
    'WminusH_M40_ctau1000' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 1000,
    },
    'WminusH_M40_ctau10000' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-40_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 10000,
    },

    'WminusH_M55_ctau0' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 0,
    },
    'WminusH_M55_ctau0p05' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 0.05,
    },

    'WminusH_M55_ctau1' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 1,
    },
    'WminusH_M55_ctau10' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 10,
    },
    'WminusH_M55_ctau100' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 100,
    },
    'WminusH_M55_ctau1000' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 1000,
    },
    'WminusH_M55_ctau10000' : {
        'files' : ['WminusH_HToSSTobbbb_WToLNu_MH-125_MS-55_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 10000,
    },
    
    #ZH Pi Pi
    'ZH_M15_ctau0' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 0,
    },
    'ZH_M15_ctau0p05' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 0.05,
    },
    'ZH_M15_ctau1' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 1,
    },
    'ZH_M15_ctau10' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 10,
    },
    'ZH_M15_ctau100' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 100,
    },
    'ZH_M15_ctau1000' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 1000,
    },
    'ZH_M15_ctau10000' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 10000,
    },

    'ZH_M40_ctau0' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 0,
    },
    'ZH_M40_ctau0p05' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 0.05,
    },
    'ZH_M40_ctau1' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 1,
    },
    'ZH_M40_ctau10' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 10,
    },
    'ZH_M40_ctau100' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 100,
    },
    'ZH_M40_ctau1000' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 1000,
    },
    'ZH_M40_ctau10000' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 10000,
    },

    'ZH_M55_ctau0' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 0,
    },
    'ZH_M55_ctau0p05' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 0.05,
    },

    'ZH_M55_ctau1' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 1,
    },
    'ZH_M55_ctau10' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 10,
    },
    'ZH_M55_ctau100' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 100,
    },
    'ZH_M55_ctau1000' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 1000,
    },
    'ZH_M55_ctau10000' : {
        'files' : ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 10000,
    },
    #ggZH Pi Pi
    'ggZH_M15_ctau0' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 0,
    },
    'ggZH_M15_ctau0p05' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 0.05,
    },
    'ggZH_M15_ctau1' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 1,
    },
    'ggZH_M15_ctau10' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 10,
    },
    'ggZH_M15_ctau100' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 100,
    },
    'ggZH_M15_ctau1000' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 1000,
    },
    'ggZH_M15_ctau10000' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 15,
        'ctau' : 10000,
    },

    'ggZH_M40_ctau0' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 0,
    },
    'ggZH_M40_ctau0p05' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 0.05,
    },
    'ggZH_M40_ctau1' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 1,
    },
    'ggZH_M40_ctau10' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 10,
    },
    'ggZH_M40_ctau100' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 100,
    },
    'ggZH_M40_ctau1000' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 1000,
    },
    'ggZH_M40_ctau10000' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 40,
        'ctau' : 10000,
    },

    'ggZH_M55_ctau0' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 0,
    },
    'ggZH_M55_ctau0p05' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 0.05,
    },
    'ggZH_M55_ctau1' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 1,
    },
    'ggZH_M55_ctau10' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 10,
    },
    'ggZH_M55_ctau100' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 100,
    },
    'ggZH_M55_ctau1000' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 1000,
    },
    'ggZH_M55_ctau10000' : {
        'files' : ['ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8'],
        'mass' : 55,
        'ctau' : 10000,
    },
#VBF
    'VBFH_M40_ctau0' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 0.001,
    },
    'VBFH_M40_ctau0p05' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0p05_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 0.05,
    },
    'VBFH_M40_ctau0p1' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0p1_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 0.1,
    },
    'VBFH_M40_ctau1' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-1_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 1,
    },
    'VBFH_M40_ctau5' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 5,
    },
    'VBFH_M40_ctau10' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-10_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 10,
    },
    'VBFH_M40_ctau25' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-25_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 25,
    },
    'VBFH_M40_ctau50' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-50_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 50,
    },
    'VBFH_M40_ctau100' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-100_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 100,
    },
    'VBFH_M40_ctau500' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-500_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 500,
    },
    'VBFH_M40_ctau1000' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-1000_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 1000,
    },
    'VBFH_M40_ctau2000' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-2000_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 2000,
    },
    'VBFH_M40_ctau5000' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5000_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 5000,
    },
    'VBFH_M40_ctau10000' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-10000_Summer16_MINIAOD'],
        'mass' : 40,
        'ctau' : 10000,
    },

#m15
    'VBFH_M15_ctau0' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-0_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 0.001,
    },
    'VBFH_M15_ctau0p05' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-0p05_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 0.05,
    },
    'VBFH_M15_ctau0p1' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-0p1_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 0.1,
    },
    'VBFH_M15_ctau1' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-1_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 1,
    },
    'VBFH_M15_ctau5' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-5_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 5,
    },
    'VBFH_M15_ctau10' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-10_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 10,
    },
    'VBFH_M15_ctau25' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-25_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 25,
    },
    'VBFH_M15_ctau50' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-50_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 50,
    },
    'VBFH_M15_ctau100' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-100_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 100,
    },
    'VBFH_M15_ctau500' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-500_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 500,
    },
    'VBFH_M15_ctau1000' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-1000_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 1000,
    },
    'VBFH_M15_ctau2000' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-2000_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 2000,
    },
    'VBFH_M15_ctau5000' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-5000_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 5000,
    },
    'VBFH_M15_ctau10000' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-10000_Summer16_MINIAOD'],
        'mass' : 15,
        'ctau' : 10000,
    },

#VBF true higgs
    'VBF_Higgs' : {
        'files' : ['VBFHToBB_M-125_13TeV_powheg_pythia8'],
        'mass' : 40,
        'ctau' : 0.005,
    },

    ### W' -> Whad Zinv
    'XWZInv_M3000' : {
        'order' : 1001,
        'files' : ['WprimeToWZToWhadZinv_narrow_M-3000_13TeV-madgraph-v1'],
        'fillcolor' : 626,#845,#67, #632 e' un rosso molto acceso,630 scuro,631 marrone, 633 meno acceso ma forte, 629-628 accesi,625 chiaro
        'fillstyle' : 0,#3344,####3005,
        'linecolor' : 626,#845,#67,
        'linewidth' : 3,
        'linestyle' : 1,
#        'label' : "m_{W^{'}} = 3 TeV (#sigma=1 pb)",
        'label' : "m_{W'} = 3 TeV (10 pb)",
        'weight': 1.,
        'plot': True,
    },
    
}
