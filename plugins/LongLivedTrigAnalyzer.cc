// -*- C++ -*-
//
// Package:    Trigger2017/LongLivedTrigAnalyzer
// Class:      LongLivedTrigAnalyzer
// 
/**\class LongLivedTrigAnalyzer LongLivedTrigAnalyzer.cc Trigger2017/LongLivedTrigAnalyzer/plugins/LongLivedTrigAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Lisa Benato
//         Created:  Sat, 08 Jul 2017 16:26:05 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "TTree.h"
#include <string>
//#include "LongLivedTrigAnalyzer.h"
//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class LongLivedTrigAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit LongLivedTrigAnalyzer(const edm::ParameterSet&);
      ~LongLivedTrigAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
      virtual bool isLooseJet(pat::Jet&);
      virtual bool isTightJet(pat::Jet&);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      bool passIDWP(std::string, bool, float, float, float, float, float, float, float, bool, int);

      // ----------member data ---------------------------
    edm::EDGetTokenT<edm::TriggerResults> trigResultsToken;
    edm::EDGetTokenT<edm::TriggerResults> filterResultsToken;
    edm::EDGetTokenT<bool> badChCandFilterToken;
    edm::EDGetTokenT<bool> badPFMuonFilterToken;
    edm::EDGetTokenT<pat::METCollection> metToken;
    edm::EDGetTokenT<pat::JetCollection> jetToken;
    edm::EDGetTokenT<pat::JetCollection> fatjetToken;
    edm::EDGetTokenT<pat::MuonCollection> muonToken;
    edm::EDGetTokenT<reco::VertexCollection> vertexToken;
    edm::EDGetTokenT<pat::ElectronCollection> electronToken;


    TTree* tree;
    bool isVerbose;
    bool isMC;
    long int EventNumber, LumiNumber, RunNumber, nPV;
    float muon1_pt, muon1_pfIso04, electron1_pt, fatjet1_pt, jet1_pt;
    float met_pt, met_pt_nomu_L, met_pt_nomu_T, m_ht, m_ht_nomu_L, m_ht_nomu_T, min_met_mht, min_met_mht_nomu_L, min_met_mht_nomu_T, met_phi, met_phi_nomu_L, met_phi_nomu_T;
    bool fatjet1_isLoose, fatjet1_isTight, muon1_isLoose, muon1_isTight;
    long int nTightMuons, nTightElectrons, nTightFatJets, nLooseMuons, nLooseElectrons, nLooseFatJets, nLooseJets, nTightJets;
    bool   trig_bit_pfmet110_pfmht110;
    bool   trig_bit_pfmet120_pfmht120;
    bool   trig_bit_pfmet120_pfmht120_PFHT60;
    bool   trig_bit_pfmet130_pfmht130;
    bool   trig_bit_pfmet140_pfmht140;
    bool   trig_bit_pfmetTypeOne110_pfmht110;
    bool   trig_bit_pfmetTypeOne120_pfmht120;
    bool   trig_bit_pfmetTypeOne120_pfmht120_PFHT60;
    bool   trig_bit_pfmetTypeOne130_pfmht130;
    bool   trig_bit_pfmetTypeOne140_pfmht140;
    bool   trig_bit_pfmetnomu110_pfmhtnomu110;
    bool   trig_bit_pfmetnomu120_pfmhtnomu120;
    bool   trig_bit_pfmetnomu120_pfmhtnomu120_PFHT60;
    bool   trig_bit_pfmetnomu130_pfmhtnomu130;
    bool   trig_bit_pfmetnomu140_pfmhtnomu140;
    bool   trig_bit_ele27_wptight_gsf;
    bool   trig_bit_isomu24;
  //Single Mu
  bool   trig_bit_IsoMu24_v;
  bool   trig_bit_IsoTkMu24_v;
  bool   trig_bit_Mu50_v;
  bool   trig_bit_Mu55_v;
  //Single Ele
  bool   trig_bit_Ele27_WPTight_Gsf_v;
  //Lepton + jets/HT
  bool   trig_bit_Ele27_WPLoose_Gsf_WHbbBoost_v;
  bool   trig_bit_Ele27_eta2p1_WPLoose_Gsf_HT200_v;
  bool   trig_bit_Mu3_PFJet40_v;
  bool   trig_bit_Ele8_CaloIdM_TrackIdM_PFJet30_v;
  bool   trig_bit_Ele17_CaloIdM_TrackIdM_PFJet30_v;
  bool   trig_bit_Ele23_CaloIdM_TrackIdM_PFJet30_v;
  bool   trig_bit_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v;
  bool   trig_bit_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v;
  //jet + met
  bool   trig_bit_PFHT350_PFMET100_JetIdCleaned_v;
  //H to bb
  //bool   trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v;
  //    bool   trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq460//prescaled to 0
  bool   trig_bit_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v;
  //    bool   trig_bit_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v//prescaled
  bool   trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v;
  bool   trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v;
  bool   trig_bit_QuadPFJet45_TripleBtagCSV_p087_v;
  bool   trig_bit_QuadPFJet45_DoubleBtagCSV_p087_v; //prescaled
  //    bool   trig_bit_QuadPFJet_DoubleBTagCSV_p016_p11_VBF_Mqq200//?
  //    bool   trig_bit_QuadPFJet_DoubleBTagCSV_p016_p11_VBF_Mqq240//?
  bool   trig_bit_QuadPFJet_VBF_v; //super prescaled
  bool   trig_bit_L1_TripleJet_VBF_v; //super prescaled
  //pfjets
  //    bool   trig_bit_PFJet40//prescaled
  //    bool   trig_bit_PFJet60//prescaled
  //    bool   trig_bit_PFJet80//prescaled
  //    bool   trig_bit_PFJet200//prescaled
  bool   trig_bit_PFJet450_v;
  bool   trig_bit_PFJet500_v;
  bool   trig_bit_DiPFJetAve40_v;//prescaled
  bool   trig_bit_DiPFJetAve60_v;//prescaled
  bool   trig_bit_DiPFJetAve80_v;//prescaled
  //Displaced things:
  bool   trig_bit_VBF_DisplacedJet40_DisplacedTrack_v;
  bool   trig_bit_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v;
  bool   trig_bit_VBF_DisplacedJet40_TightID_DisplacedTrack_v;
  bool   trig_bit_VBF_DisplacedJet40_Hadronic_v; //prescaled to 0
  bool   trig_bit_VBF_DisplacedJet40_Hadronic_2PromptTrack_v; //prescaled to 0
  bool   trig_bit_VBF_DisplacedJet40_TightID_Hadronic_v; //prescaled to 0
  bool   trig_bit_VBF_DisplacedJet40_VTightID_Hadronic_v;
  bool   trig_bit_VBF_DisplacedJet40_VVTightID_Hadronic_v;
  bool   trig_bit_VBF_DisplacedJet40_VTightID_DisplacedTrack_v;
  bool   trig_bit_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v;
  bool   trig_bit_HT650_DisplacedDijet80_Inclusive_v;
  bool   trig_bit_HT750_DisplacedDijet80_Inclusive_v;
  bool   trig_bit_HT350_DisplacedDijet40_DisplacedTrack_v;
  bool   trig_bit_HT250_DisplacedDijet40_DisplacedTrack_v; //prescaled
  bool   trig_bit_HT350_DisplacedDijet80_Tight_DisplacedTrack_v;
  //Mu + jets displaced
  bool   trig_bit_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight_v;
  bool   trig_bit_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v;
  bool   trig_bit_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v;
  bool   trig_bit_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v;
  bool   trig_bit_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v;
  bool   trig_bit_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v;
  bool   trig_bit_Mu28NoFiltersNoVtx_CentralCaloJet40_v;
  //HT and various jets
  //    bool   trig_bit_HT200_v//hardly prescaled
  //    bool   trig_bit_HT275_v//prescaled
  //    bool   trig_bit_HT325_v//prescaled
  //    bool   trig_bit_HT425_v//prescaled
  //    bool   trig_bit_HT575_v//prescaled
  bool   trig_bit_HT650_v;
  bool   trig_bit_PFHT800_v; //first unprescaled
  bool   trig_bit_PFHT550_4JetPt50_v;
  bool   trig_bit_PFHT650_4JetPt50_v;
  bool   trig_bit_PFHT750_4JetPt50_v;
  bool   trig_bit_PFHT800_4JetPt50_v;
  bool   trig_bit_PFHT850_4JetPt50_v;
  bool   trig_bit_PFJet15_NoCaloMatched_v;
  bool   trig_bit_PFJet25_NoCaloMatched_v;
  bool   trig_bit_DiPFJet15_NoCaloMatched_v;
  bool   trig_bit_DiPFJet25_NoCaloMatched_v;
  bool   trig_bit_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v;
  bool   trig_bit_DiCentralPFJet430_v;
  bool   trig_bit_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v;
  bool   trig_bit_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v;
  bool   trig_bit_PFHT650_WideJetMJJ900DEtaJJ1p5_v;
  bool   trig_bit_PFHT650_WideJetMJJ950DEtaJJ1p5_v;
  //Calo jets
  bool   trig_bit_CaloJet260_v; 
  bool   trig_bit_CaloJet500_NoJetID_v; 
  bool   trig_bit_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v; 
  bool   trig_bit_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v; 
  bool   trig_bit_HT250_CaloMET70_v; 


    //MET filters
    bool trig_bit_flag_HBHENoiseFilter;
    bool trig_bit_flag_HBHENoiseIsoFilter;
    bool trig_bit_flag_EcalDeadCellTriggerPrimitiveFilter;
    bool trig_bit_flag_goodVertices;
    bool trig_bit_flag_eeBadScFilter;
    bool trig_bit_flag_globalSuperTightHalo2016Filter;
    bool flag_BadChCand;
    bool flag_BadPFMuon;
};


//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
LongLivedTrigAnalyzer::LongLivedTrigAnalyzer(const edm::ParameterSet& iConfig)

{

    //Input tags
    edm::InputTag IT_trigResults = edm::InputTag("TriggerResults::HLT");
    trigResultsToken= consumes<edm::TriggerResults>(IT_trigResults);
    edm::InputTag IT_filterResults = edm::InputTag("TriggerResults::RECO");
    filterResultsToken= consumes<edm::TriggerResults>(IT_filterResults);

    edm::InputTag IT_badChCandFilter = edm::InputTag("BadChargedCandidateFilter");
    badChCandFilterToken= consumes<bool>(IT_badChCandFilter);
    edm::InputTag IT_badPFMuonFilter = edm::InputTag("BadPFMuonFilter");
    badPFMuonFilterToken= consumes<bool>(IT_badPFMuonFilter);

    edm::InputTag IT_met = edm::InputTag("slimmedMETs");
    metToken = consumes<pat::METCollection>(IT_met);
    edm::InputTag IT_jets = edm::InputTag("slimmedJets");
    jetToken = consumes<pat::JetCollection>(IT_jets);
    edm::InputTag IT_fatjets = edm::InputTag("slimmedJetsAK8");
    fatjetToken = consumes<pat::JetCollection>(IT_fatjets);
    edm::InputTag IT_vertices = edm::InputTag("offlineSlimmedPrimaryVertices");
    vertexToken = consumes<reco::VertexCollection>(IT_vertices);
    edm::InputTag IT_muons = edm::InputTag("slimmedMuons");
    muonToken = consumes<pat::MuonCollection>(IT_muons);
    edm::InputTag IT_electrons = edm::InputTag("slimmedElectrons");
    electronToken = consumes<pat::ElectronCollection>(IT_electrons);

    isVerbose = iConfig.getParameter<bool> ("verbose");

    //now do what ever initialization is needed
    usesResource("TFileService");

    edm::Service<TFileService> fs;
    tree = fs->make<TTree>("tree", "tree");
    tree -> Branch("isMC" , &isMC, "isMC/O");
    tree -> Branch("EventNumber" , &EventNumber , "EventNumber/L");
    tree -> Branch("LumiNumber" , &LumiNumber , "LumiNumber/L");
    tree -> Branch("RunNumber" , &RunNumber , "RunNumber/L");
    tree -> Branch("nPV" , &nPV , "nPV/L");
    tree -> Branch("nLooseMuons" , &nLooseMuons , "nLooseMuons/L");
    tree -> Branch("nLooseElectrons" , &nLooseElectrons , "nLooseElectrons/L");
    tree -> Branch("nLooseFatJets" , &nLooseFatJets , "nLooseFatJets/L");
    tree -> Branch("nLooseJets" , &nLooseJets , "nLooseJets/L");
    tree -> Branch("nTightMuons" , &nTightMuons , "nTightMuons/L");
    tree -> Branch("nTightElectrons" , &nTightElectrons , "nTightElectrons/L");
    tree -> Branch("nTightFatJets" , &nTightFatJets , "nTightFatJets/L");
    tree -> Branch("nTightJets" , &nTightJets , "nTightJets/L");
    tree -> Branch("Muon1_pt", &muon1_pt, "Muon1_pt/F");
    tree -> Branch("Muon1_isLoose", &muon1_isLoose, "Muon1_isLoose/B");
    tree -> Branch("Muon1_isTight", &muon1_isTight, "Muon1_isTight/B");
    tree -> Branch("Muon1_pfIso04", &muon1_pfIso04, "Muon1_pfIso04/F");
    tree -> Branch("Electron1_pt", &electron1_pt, "Electron1_pt/F");
    tree -> Branch("FatJet1_pt", &fatjet1_pt, "FatJet1_pt/F");
    tree -> Branch("FatJet1_isLoose", &fatjet1_isLoose, "FatJet1_isLoose/B");
    tree -> Branch("FatJet1_isTight", &fatjet1_isTight, "FatJet1_isTight/B");
    tree -> Branch("Jet1_pt", &jet1_pt, "Jet1_pt/F");
    tree -> Branch("MEt_pt", &met_pt, "MEt_pt/F");
    tree -> Branch("MEt_phi", &met_phi, "MEt_phi/F");
    tree -> Branch("m_ht", &m_ht, "m_ht/F");
    tree -> Branch("m_ht_nomu_L", &m_ht_nomu_L, "m_ht_nomu_L/F");
    tree -> Branch("m_ht_nomu_T", &m_ht_nomu_T, "m_ht_nomu_T/F");
    tree -> Branch("min_met_mht", &min_met_mht, "min_met_mht/F");
    tree -> Branch("met_pt_nomu_L", &met_pt_nomu_L, "met_pt_nomu_L/F");
    tree -> Branch("met_pt_nomu_T", &met_pt_nomu_T, "met_pt_nomu_T/F");
    tree -> Branch("min_met_mht_nomu_L", &min_met_mht_nomu_L, "min_met_mht_nomu_L/F");
    tree -> Branch("min_met_mht_nomu_T", &min_met_mht_nomu_T, "min_met_mht_nomu_T/F");
    tree -> Branch("HLT_PFMET110_PFMHT110_IDTight_v", &trig_bit_pfmet110_pfmht110, "HLT_PFMET110_PFMHT110_IDTight_v/B");
    tree -> Branch("HLT_PFMET120_PFMHT120_IDTight_v", &trig_bit_pfmet120_pfmht120, "HLT_PFMET120_PFMHT120_IDTight_v/B");
    tree -> Branch("HLT_PFMET120_PFMHT120_IDTight_PFHT60_v", &trig_bit_pfmet120_pfmht120_PFHT60, "HLT_PFMET120_PFMHT120_IDTight_PFHT60_v/B");
    tree -> Branch("HLT_PFMET130_PFMHT130_IDTight_v", &trig_bit_pfmet130_pfmht130, "HLT_PFMET130_PFMHT130_IDTight_v/B");
    tree -> Branch("HLT_PFMET140_PFMHT140_IDTight_v", &trig_bit_pfmet140_pfmht140, "HLT_PFMET140_PFMHT140_IDTight_v/B");
    tree -> Branch("HLT_PFMETTypeOne110_PFMHT110_IDTight_v", &trig_bit_pfmetTypeOne110_pfmht110, "HLT_PFMETTypeOne110_PFMHT110_IDTight_v/B");
    tree -> Branch("HLT_PFMETTypeOne120_PFMHT120_IDTight_v", &trig_bit_pfmetTypeOne120_pfmht120, "HLT_PFMETTypeOne120_PFMHT120_IDTight_v/B");
    tree -> Branch("HLT_PFMETTypeOne120_PFMHT120_IDTight_PFHT60_v", &trig_bit_pfmetTypeOne120_pfmht120_PFHT60, "HLT_PFMETTypeOne120_PFMHT120_IDTight_PFHT60_v/B");
    tree -> Branch("HLT_PFMETTypeOne130_PFMHT130_IDTight_v", &trig_bit_pfmetTypeOne130_pfmht130, "HLT_PFMETTypeOne130_PFMHT130_IDTight_v/B");
    tree -> Branch("HLT_PFMETTypeOne140_PFMHT140_IDTight_v", &trig_bit_pfmetTypeOne140_pfmht140, "HLT_PFMETTypeOne140_PFMHT140_IDTight_v/B");
    tree -> Branch("HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v", &trig_bit_pfmetnomu110_pfmhtnomu110, "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v/B");
    tree -> Branch("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v", &trig_bit_pfmetnomu120_pfmhtnomu120, "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v/B");
    tree -> Branch("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v", &trig_bit_pfmetnomu120_pfmhtnomu120_PFHT60, "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v/B");
    tree -> Branch("HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v", &trig_bit_pfmetnomu130_pfmhtnomu130, "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v/B");
    tree -> Branch("HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v", &trig_bit_pfmetnomu140_pfmhtnomu140, "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v/B");
  //Single Mu
    tree -> Branch("HLT_IsoMu24_v", &trig_bit_IsoMu24_v, "HLT_IsoMu24_v/B");
    tree -> Branch("HLT_IsoTkMu24_v", &trig_bit_IsoTkMu24_v, "HLT_IsoTkMu24_v/B");
    tree -> Branch("HLT_Mu50_v", &trig_bit_Mu50_v, "HLT_Mu50_v/B");
    tree -> Branch("HLT_Mu55_v", &trig_bit_Mu55_v, "HLT_Mu55_v/B");
  //Single Ele
    tree -> Branch("HLT_Ele27_WPTight_Gsf_v", &trig_bit_Ele27_WPTight_Gsf_v, "HLT_Ele27_WPTight_Gsf_v/B");
  //Lepton + jets/HT
    tree -> Branch("HLT_Ele27_WPLoose_Gsf_WHbbBoost_v", &trig_bit_Ele27_WPLoose_Gsf_WHbbBoost_v, "HLT_Ele27_WPLoose_Gsf_WHbbBoost_v/B");
    tree -> Branch("HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v", &trig_bit_Ele27_eta2p1_WPLoose_Gsf_HT200_v, "HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v/B");
    tree -> Branch("HLT_Mu3_PFJet40_v", &trig_bit_Mu3_PFJet40_v, "HLT_Mu3_PFJet40_v/B");
    tree -> Branch("HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v", &trig_bit_Ele8_CaloIdM_TrackIdM_PFJet30_v, "HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v/B");
    tree -> Branch("HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v", &trig_bit_Ele17_CaloIdM_TrackIdM_PFJet30_v, "HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v/B");
    tree -> Branch("HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v", &trig_bit_Ele23_CaloIdM_TrackIdM_PFJet30_v, "HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v/B");
    tree -> Branch("HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v", &trig_bit_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v, "HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v/B");
    tree -> Branch("HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v", &trig_bit_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v, "HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v/B");
  //jet + met
    tree -> Branch("HLT_PFHT350_PFMET100_JetIdCleaned_v", &trig_bit_PFHT350_PFMET100_JetIdCleaned_v, "HLT_PFHT350_PFMET100_JetIdCleaned_v/B");
  //H to bb
    tree -> Branch("HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v", &trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v, "HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v/B");
    tree -> Branch("HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v", &trig_bit_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v, "HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v/B");
    tree -> Branch("HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v", &trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v, "HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v/B");
    tree -> Branch("HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v", &trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v, "HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v/B");
    tree -> Branch("HLT_QuadPFJet45_TripleBtagCSV_p087_v", &trig_bit_QuadPFJet45_TripleBtagCSV_p087_v, "HLT_QuadPFJet45_TripleBtagCSV_p087_v/B");
    tree -> Branch("HLT_QuadPFJet45_DoubleBtagCSV_p087_v", &trig_bit_QuadPFJet45_DoubleBtagCSV_p087_v, "HLT_QuadPFJet45_DoubleBtagCSV_p087_v/B");
    tree -> Branch("HLT_QuadPFJet_VBF_v", &trig_bit_QuadPFJet_VBF_v, "HLT_QuadPFJet_VBF_v/B");//super prescaled
    tree -> Branch("HLT_L1_TripleJet_VBF_v", &trig_bit_L1_TripleJet_VBF_v, "HLT_L1_TripleJet_VBF_v/B");//super prescaled
  //pfjets
    tree -> Branch("HLT_PFJet450_v", &trig_bit_PFJet450_v, "HLT_PFJet450_v/B");
    tree -> Branch("HLT_PFJet500_v", &trig_bit_PFJet500_v, "HLT_PFJet500_v/B");
    tree -> Branch("HLT_DiPFJetAve40_v", &trig_bit_DiPFJetAve40_v, "HLT_DiPFJetAve40_v/B");//prescaled
    tree -> Branch("HLT_DiPFJetAve60_v", &trig_bit_DiPFJetAve60_v, "HLT_DiPFJetAve60_v/B");//prescaled
    tree -> Branch("HLT_DiPFJetAve80_v", &trig_bit_DiPFJetAve80_v, "HLT_DiPFJetAve80_v/B");//prescaled
  //Displaced things:
    tree -> Branch("HLT_VBF_DisplacedJet40_DisplacedTrack_v", &trig_bit_VBF_DisplacedJet40_DisplacedTrack_v, "HLT_VBF_DisplacedJet40_DisplacedTrack_v/B");
    tree -> Branch("HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v", &trig_bit_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v, "HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v/B");
    tree -> Branch("HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v", &trig_bit_VBF_DisplacedJet40_TightID_DisplacedTrack_v, "HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v/B");
    tree -> Branch("HLT_VBF_DisplacedJet40_VTightID_Hadronic_v", &trig_bit_VBF_DisplacedJet40_VTightID_Hadronic_v, "HLT_VBF_DisplacedJet40_VTightID_Hadronic_v/B");
    tree -> Branch("HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v", &trig_bit_VBF_DisplacedJet40_VVTightID_Hadronic_v, "HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v/B");
    tree -> Branch("HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v", &trig_bit_VBF_DisplacedJet40_VTightID_DisplacedTrack_v, "HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v/B");
    tree -> Branch("HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v", &trig_bit_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v, "HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v/B");
    tree -> Branch("HLT_HT650_DisplacedDijet80_Inclusive_v", &trig_bit_HT650_DisplacedDijet80_Inclusive_v, "HLT_HT650_DisplacedDijet80_Inclusive_v/B");
    tree -> Branch("HLT_HT750_DisplacedDijet80_Inclusive_v", &trig_bit_HT750_DisplacedDijet80_Inclusive_v, "HLT_HT750_DisplacedDijet80_Inclusive_v/B");
    tree -> Branch("HLT_HT350_DisplacedDijet40_DisplacedTrack_v", &trig_bit_HT350_DisplacedDijet40_DisplacedTrack_v, "HLT_HT350_DisplacedDijet40_DisplacedTrack_v/B");
    tree -> Branch("HLT_HT250_DisplacedDijet40_DisplacedTrack_v", &trig_bit_HT250_DisplacedDijet40_DisplacedTrack_v, "HLT_HT250_DisplacedDijet40_DisplacedTrack_v/B");//prescaled;
    tree -> Branch("HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v", &trig_bit_HT350_DisplacedDijet80_Tight_DisplacedTrack_v, "HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v/B");
  //Mu + jets displaced
    tree -> Branch("HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight_v", &trig_bit_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight_v, "HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight_v/B");
    tree -> Branch("HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v", &trig_bit_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v, "HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v/B");
    tree -> Branch("HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v", &trig_bit_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v, "HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v/B");
    tree -> Branch("HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v", &trig_bit_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v, "HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v/B");
    tree -> Branch("HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v", &trig_bit_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v, "HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v/B");
    tree -> Branch("HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v", &trig_bit_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v, "HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v/B");
    tree -> Branch("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v", &trig_bit_Mu28NoFiltersNoVtx_CentralCaloJet40_v, "HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v/B");
    tree -> Branch("HLT_HT650_v", &trig_bit_HT650_v, "HLT_HT650_v/B");
    tree -> Branch("HLT_PFHT800_v", &trig_bit_PFHT800_v, "HLT_PFHT800_v/B");
    tree -> Branch("HLT_PFHT550_4JetPt50_v", &trig_bit_PFHT550_4JetPt50_v, "HLT_PFHT550_4JetPt50_v/B");
    tree -> Branch("HLT_PFHT650_4JetPt50_v", &trig_bit_PFHT650_4JetPt50_v, "HLT_PFHT650_4JetPt50_v/B");
    tree -> Branch("HLT_PFHT750_4JetPt50_v", &trig_bit_PFHT750_4JetPt50_v, "HLT_PFHT750_4JetPt50_v/B");
    tree -> Branch("HLT_PFHT800_4JetPt50_v", &trig_bit_PFHT800_4JetPt50_v, "HLT_PFHT800_4JetPt50_v/B");
    tree -> Branch("HLT_PFHT850_4JetPt50_v", &trig_bit_PFHT850_4JetPt50_v, "HLT_PFHT850_4JetPt50_v/B");
    tree -> Branch("HLT_PFJet15_NoCaloMatched_v", &trig_bit_PFJet15_NoCaloMatched_v, "HLT_PFJet15_NoCaloMatched_v/B");
    tree -> Branch("HLT_PFJet25_NoCaloMatched_v", &trig_bit_PFJet25_NoCaloMatched_v, "HLT_PFJet25_NoCaloMatched_v/B");
    tree -> Branch("HLT_DiPFJet15_NoCaloMatched_v", &trig_bit_DiPFJet15_NoCaloMatched_v, "HLT_DiPFJet15_NoCaloMatched_v/B");
    tree -> Branch("HLT_DiPFJet25_NoCaloMatched_v", &trig_bit_DiPFJet25_NoCaloMatched_v, "HLT_DiPFJet25_NoCaloMatched_v/B");
    tree -> Branch("HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v", &trig_bit_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v, "HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v/B");
    tree -> Branch("HLT_DiCentralPFJet430_v", &trig_bit_DiCentralPFJet430_v, "HLT_DiCentralPFJet430_v/B");
    tree -> Branch("HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v", &trig_bit_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v, "HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v/B");
    tree -> Branch("HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v", &trig_bit_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v, "HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v/B");
    tree -> Branch("HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v", &trig_bit_PFHT650_WideJetMJJ900DEtaJJ1p5_v, "HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v/B");
    tree -> Branch("HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v", &trig_bit_PFHT650_WideJetMJJ950DEtaJJ1p5_v, "HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v/B");
    tree -> Branch("HLT_CaloJet260_v", &trig_bit_CaloJet260_v, "HLT_CaloJet260_v/B"); 
    tree -> Branch("HLT_CaloJet500_NoJetID_v", &trig_bit_CaloJet500_NoJetID_v, "HLT_CaloJet500_NoJetID_v/B");
    tree -> Branch("HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v", &trig_bit_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v, "HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v/B"); 
    tree -> Branch("HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v", &trig_bit_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v, "HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v/B"); 
    tree -> Branch("HLT_HT250_CaloMET70_v", &trig_bit_HT250_CaloMET70_v, "HLT_HT250_CaloMET70_v/B");


    tree -> Branch("HLT_Ele27_WPTight_Gsf_v", &trig_bit_ele27_wptight_gsf, "HLT_Ele27_WPTight_Gsf_v/B");
    tree -> Branch("HLT_IsoMu24_v", &trig_bit_isomu24, "HLT_IsoMu24_v/B");
    tree -> Branch("Flag_HBHENoiseFilter", &trig_bit_flag_HBHENoiseFilter, "Flag_HBHENoiseFilter/B");
    tree -> Branch("Flag_HBHENoiseIsoFilter", &trig_bit_flag_HBHENoiseIsoFilter, "Flag_HBHENoiseIsoFilter/B");
    tree -> Branch("Flag_EcalDeadCellTriggerPrimitiveFilter", &trig_bit_flag_EcalDeadCellTriggerPrimitiveFilter, "Flag_EcalDeadCellTriggerPrimitiveFilter/B");
    tree -> Branch("Flag_goodVertices", &trig_bit_flag_goodVertices, "Flag_goodVertices/B");
    tree -> Branch("Flag_eeBadScFilter", &trig_bit_flag_eeBadScFilter, "Flag_eeBadScFilter/B");
    tree -> Branch("Flag_globalSuperTightHalo2016Filter", &trig_bit_flag_globalSuperTightHalo2016Filter, "Flag_globalSuperTightHalo2016Filter/B");
    tree -> Branch("Flag_BadChCand", &flag_BadChCand, "Flag_BadChCand/B");
    tree -> Branch("Flag_BadPFMuon", &flag_BadPFMuon, "Flag_BadPFMuon/B");

}


LongLivedTrigAnalyzer::~LongLivedTrigAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
LongLivedTrigAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    using namespace reco;
    using namespace std;

    isMC = false;
    EventNumber = LumiNumber = RunNumber = nPV = 0;
    nTightMuons = nTightElectrons = nTightFatJets = nLooseMuons = nLooseElectrons = nLooseFatJets = 0;

    trig_bit_pfmet110_pfmht110 = false;
    trig_bit_pfmet120_pfmht120 = false;
    trig_bit_pfmet120_pfmht120_PFHT60 = false;
    trig_bit_pfmet130_pfmht130 = false;
    trig_bit_pfmet140_pfmht140 = false;
    trig_bit_pfmetTypeOne110_pfmht110 = false;
    trig_bit_pfmetTypeOne120_pfmht120 = false;
    trig_bit_pfmetTypeOne120_pfmht120_PFHT60 = false;
    trig_bit_pfmetTypeOne130_pfmht130 = false;
    trig_bit_pfmetTypeOne140_pfmht140 = false;
    trig_bit_pfmetnomu110_pfmhtnomu110 = false;
    trig_bit_pfmetnomu120_pfmhtnomu120 = false;
    trig_bit_pfmetnomu120_pfmhtnomu120_PFHT60 = false;
    trig_bit_pfmetnomu130_pfmhtnomu130 = false;
    trig_bit_pfmetnomu140_pfmhtnomu140 = false;
    trig_bit_ele27_wptight_gsf = false;
    trig_bit_isomu24 = false;
    trig_bit_flag_HBHENoiseFilter = false;
    trig_bit_flag_HBHENoiseIsoFilter = false;
    trig_bit_flag_EcalDeadCellTriggerPrimitiveFilter = false;
    trig_bit_flag_goodVertices = false;
    trig_bit_flag_eeBadScFilter = false;
    trig_bit_flag_globalSuperTightHalo2016Filter = false;

    trig_bit_IsoMu24_v = false;
    trig_bit_IsoTkMu24_v = false;
    trig_bit_Mu50_v = false;
    trig_bit_Mu55_v = false;
    //Single Ele
    trig_bit_Ele27_WPTight_Gsf_v = false;
    //Lepton + jets/HT
    trig_bit_Ele27_WPLoose_Gsf_WHbbBoost_v = false;
    trig_bit_Ele27_eta2p1_WPLoose_Gsf_HT200_v = false;
    trig_bit_Mu3_PFJet40_v = false;
    trig_bit_Ele8_CaloIdM_TrackIdM_PFJet30_v = false;
    trig_bit_Ele17_CaloIdM_TrackIdM_PFJet30_v = false;
    trig_bit_Ele23_CaloIdM_TrackIdM_PFJet30_v = false;
    trig_bit_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v = false;
    trig_bit_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v = false;
    //jet + met
    trig_bit_PFHT350_PFMET100_JetIdCleaned_v = false;
    //H to bb
    trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v = false;
    //  trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq460//prescaled to 0
    trig_bit_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v = false;
    //  trig_bit_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v//prescaled
    trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v = false;
    trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v = false;
    trig_bit_QuadPFJet45_TripleBtagCSV_p087_v = false;
    trig_bit_QuadPFJet45_DoubleBtagCSV_p087_v = false; //prescaled
    //  trig_bit_QuadPFJet_DoubleBTagCSV_p016_p11_VBF_Mqq200//?
    //  trig_bit_QuadPFJet_DoubleBTagCSV_p016_p11_VBF_Mqq240//?
    trig_bit_QuadPFJet_VBF_v = false; //super prescaled
    trig_bit_L1_TripleJet_VBF_v = false; //super prescaled
    //pfjets
    //  trig_bit_PFJet40//prescaled
    //  trig_bit_PFJet60//prescaled
    //  trig_bit_PFJet80//prescaled
    //  trig_bit_PFJet200//prescaled
    trig_bit_PFJet450_v = false;
    trig_bit_PFJet500_v = false;
    trig_bit_DiPFJetAve40_v = false;//prescaled
    trig_bit_DiPFJetAve60_v = false;//prescaled
    trig_bit_DiPFJetAve80_v = false;//prescaled
    //Displaced things:
    trig_bit_VBF_DisplacedJet40_DisplacedTrack_v = false;
    trig_bit_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v = false;
    trig_bit_VBF_DisplacedJet40_TightID_DisplacedTrack_v = false;
    trig_bit_VBF_DisplacedJet40_Hadronic_v = false; //prescaled to 0
    trig_bit_VBF_DisplacedJet40_Hadronic_2PromptTrack_v = false; //prescaled to 0
    trig_bit_VBF_DisplacedJet40_TightID_Hadronic_v = false; //prescaled to 0
    trig_bit_VBF_DisplacedJet40_VTightID_Hadronic_v = false;
    trig_bit_VBF_DisplacedJet40_VVTightID_Hadronic_v = false;
    trig_bit_VBF_DisplacedJet40_VTightID_DisplacedTrack_v = false;
    trig_bit_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v = false;
    trig_bit_HT650_DisplacedDijet80_Inclusive_v = false;
    trig_bit_HT750_DisplacedDijet80_Inclusive_v = false;
    trig_bit_HT350_DisplacedDijet40_DisplacedTrack_v = false;
    trig_bit_HT250_DisplacedDijet40_DisplacedTrack_v = false; //prescaled
    trig_bit_HT350_DisplacedDijet80_Tight_DisplacedTrack_v = false;
    //Mu + jets displaced
    trig_bit_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight_v = false;
    trig_bit_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v = false;
    trig_bit_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v = false;
    trig_bit_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v = false;
    trig_bit_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v = false;
    trig_bit_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v = false;
    trig_bit_Mu28NoFiltersNoVtx_CentralCaloJet40_v = false;
    //HT and various jets
    //  trig_bit_HT200_v//hardly prescaled
    //  trig_bit_HT275_v//prescaled
    //  trig_bit_HT325_v//prescaled
    //  trig_bit_HT425_v//prescaled
    //  trig_bit_HT575_v//prescaled
    trig_bit_HT650_v = false;
    trig_bit_PFHT800_v = false; //first unprescaled
    trig_bit_PFHT550_4JetPt50_v = false;
    trig_bit_PFHT650_4JetPt50_v = false;
    trig_bit_PFHT750_4JetPt50_v = false;
    trig_bit_PFHT800_4JetPt50_v = false;
    trig_bit_PFHT850_4JetPt50_v = false;
    trig_bit_PFJet15_NoCaloMatched_v = false;
    trig_bit_PFJet25_NoCaloMatched_v = false;
    trig_bit_DiPFJet15_NoCaloMatched_v = false;
    trig_bit_DiPFJet25_NoCaloMatched_v = false;
    trig_bit_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v = false;
    trig_bit_DiCentralPFJet430_v = false;
    trig_bit_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v = false;
    trig_bit_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v = false;
    trig_bit_PFHT650_WideJetMJJ900DEtaJJ1p5_v = false;
    trig_bit_PFHT650_WideJetMJJ950DEtaJJ1p5_v = false;
    //Calo jets
    trig_bit_CaloJet260_v = false;
    trig_bit_CaloJet500_NoJetID_v = false;
    trig_bit_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v = false;
    trig_bit_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v = false;
    trig_bit_HT250_CaloMET70_v = false;

    muon1_pt = 0.;
    muon1_pfIso04 = -1.;
    electron1_pt = 0.;
    muon1_isLoose = muon1_isTight = fatjet1_isLoose = fatjet1_isTight = false;
    met_pt = met_pt_nomu_L = met_pt_nomu_T = m_ht = m_ht_nomu_L = m_ht_nomu_T = min_met_mht = min_met_mht_nomu_L = min_met_mht_nomu_T = 0.;
    met_phi = met_phi_nomu_L = met_phi_nomu_T = -10.;


    //Accessing trigger bits (same as AOD); thanks to Owen Long (SUSY)
    edm::Handle<edm::TriggerResults> trigResults;
    iEvent.getByToken(trigResultsToken, trigResults);

    if( !trigResults.failedToGet() ) {
        int N_Triggers = trigResults->size();
        const edm::TriggerNames & trigName = iEvent.triggerNames(*trigResults);

        for( int i_Trig = 0; i_Trig < N_Triggers; ++i_Trig ) {
            if (trigResults.product()->accept(i_Trig)) {
              TString TrigPath =trigName.triggerName(i_Trig);

	      //if ( TrigPath.Contains("HLT_") ) std::cout << TrigPath << std::endl;
              //if ( TrigPath.Contains("") )  = true;
              if ( TrigPath.Contains("HLT_IsoMu24_v") ) trig_bit_IsoMu24_v = true;
              if ( TrigPath.Contains("HLT_IsoTkMu24_v") ) trig_bit_IsoTkMu24_v = true;
              if ( TrigPath.Contains("HLT_Mu50_v") ) trig_bit_Mu50_v = true;
              if ( TrigPath.Contains("HLT_Mu55_v") ) trig_bit_Mu55_v = true;
  //Single Ele
              if ( TrigPath.Contains("HLT_Ele27_WPTight_Gsf_v") ) trig_bit_Ele27_WPTight_Gsf_v = true;
  //Lepton + jets/HT
              if ( TrigPath.Contains("HLT_Ele27_WPLoose_Gsf_WHbbBoost_v") ) trig_bit_Ele27_WPLoose_Gsf_WHbbBoost_v = true;
              if ( TrigPath.Contains("HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v") ) trig_bit_Ele27_eta2p1_WPLoose_Gsf_HT200_v = true;
              if ( TrigPath.Contains("HLT_Mu3_PFJet40_v") ) trig_bit_Mu3_PFJet40_v = true;
              if ( TrigPath.Contains("HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v") ) trig_bit_Ele8_CaloIdM_TrackIdM_PFJet30_v = true;
              if ( TrigPath.Contains("HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v") ) trig_bit_Ele17_CaloIdM_TrackIdM_PFJet30_v = true;
              if ( TrigPath.Contains("HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v") ) trig_bit_Ele23_CaloIdM_TrackIdM_PFJet30_v = true;
              if ( TrigPath.Contains("HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v") ) trig_bit_Ele50_CaloIdVT_GsfTrkIdT_PFJet140_v = true;
              if ( TrigPath.Contains("HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v") ) trig_bit_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v = true;
  //jet + met
              if ( TrigPath.Contains("HLT_PFHT350_PFMET100_JetIdCleaned_v") ) trig_bit_PFHT350_PFMET100_JetIdCleaned_v = true;
  //H to bb
              if ( TrigPath.Contains("HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v") ) trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v = true;
              if ( TrigPath.Contains("HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v") ) trig_bit_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v = true;
              if ( TrigPath.Contains("HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v") ) trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v = true;
              if ( TrigPath.Contains("HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v") ) trig_bit_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v = true;
              if ( TrigPath.Contains("HLT_QuadPFJet45_TripleBtagCSV_p087_v") ) trig_bit_QuadPFJet45_TripleBtagCSV_p087_v = true;
              if ( TrigPath.Contains("HLT_QuadPFJet45_DoubleBtagCSV_p087_v") ) trig_bit_QuadPFJet45_DoubleBtagCSV_p087_v = true;
              if ( TrigPath.Contains("HLT_QuadPFJet_VBF_v") ) trig_bit_QuadPFJet_VBF_v = true;//super prescaled
              if ( TrigPath.Contains("HLT_L1_TripleJet_VBF_v") ) trig_bit_L1_TripleJet_VBF_v = true;//super prescaled
  //pfjets
              if ( TrigPath.Contains("HLT_PFJet450_v") ) trig_bit_PFJet450_v = true;
              if ( TrigPath.Contains("HLT_PFJet500_v") ) trig_bit_PFJet500_v = true;
              if ( TrigPath.Contains("HLT_DiPFJetAve40_v") ) trig_bit_DiPFJetAve40_v = true;//prescaled
              if ( TrigPath.Contains("HLT_DiPFJetAve60_v") ) trig_bit_DiPFJetAve60_v = true;//prescaled
              if ( TrigPath.Contains("HLT_DiPFJetAve80_v") ) trig_bit_DiPFJetAve80_v = true;//prescaled
  //Displaced things:
              if ( TrigPath.Contains("HLT_VBF_DisplacedJet40_DisplacedTrack_v") ) trig_bit_VBF_DisplacedJet40_DisplacedTrack_v = true;
              if ( TrigPath.Contains("HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v") ) trig_bit_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v = true;
              if ( TrigPath.Contains("HLT_VBF_DisplacedJet40_TightID_DisplacedTrack_v") ) trig_bit_VBF_DisplacedJet40_TightID_DisplacedTrack_v = true;
              if ( TrigPath.Contains("HLT_VBF_DisplacedJet40_VTightID_Hadronic_v") ) trig_bit_VBF_DisplacedJet40_VTightID_Hadronic_v = true;
              if ( TrigPath.Contains("HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v") ) trig_bit_VBF_DisplacedJet40_VVTightID_Hadronic_v = true;
              if ( TrigPath.Contains("HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v") ) trig_bit_VBF_DisplacedJet40_VTightID_DisplacedTrack_v = true;
              if ( TrigPath.Contains("HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v") ) trig_bit_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v = true;
              if ( TrigPath.Contains("HLT_HT650_DisplacedDijet80_Inclusive_v") ) trig_bit_HT650_DisplacedDijet80_Inclusive_v = true;
              if ( TrigPath.Contains("HLT_HT750_DisplacedDijet80_Inclusive_v") ) trig_bit_HT750_DisplacedDijet80_Inclusive_v = true;
              if ( TrigPath.Contains("HLT_HT350_DisplacedDijet40_DisplacedTrack_v") ) trig_bit_HT350_DisplacedDijet40_DisplacedTrack_v = true;
              if ( TrigPath.Contains("HLT_HT250_DisplacedDijet40_DisplacedTrack_v") ) trig_bit_HT250_DisplacedDijet40_DisplacedTrack_v = true;//prescaled = true;
              if ( TrigPath.Contains("HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v") ) trig_bit_HT350_DisplacedDijet80_Tight_DisplacedTrack_v = true;
  //Mu + jets displaced
              if ( TrigPath.Contains("HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight_v") ) trig_bit_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Tight_v = true;
              if ( TrigPath.Contains("HLT_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v") ) trig_bit_Mu33NoFiltersNoVtxDisplaced_DisplacedJet50_Loose_v = true;
              if ( TrigPath.Contains("HLT_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v") ) trig_bit_Mu28NoFiltersNoVtx_DisplacedJet40_Loose_v = true;
              if ( TrigPath.Contains("HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v") ) trig_bit_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v = true;
              if ( TrigPath.Contains("HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v") ) trig_bit_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v = true;
              if ( TrigPath.Contains("HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v") ) trig_bit_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v = true;
              if ( TrigPath.Contains("HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v") ) trig_bit_Mu28NoFiltersNoVtx_CentralCaloJet40_v = true;
              if ( TrigPath.Contains("HLT_HT650_v") ) trig_bit_HT650_v = true;
              if ( TrigPath.Contains("HLT_PFHT800_v") ) trig_bit_PFHT800_v = true;
              if ( TrigPath.Contains("HLT_PFHT550_4JetPt50_v") ) trig_bit_PFHT550_4JetPt50_v = true;
              if ( TrigPath.Contains("HLT_PFHT650_4JetPt50_v") ) trig_bit_PFHT650_4JetPt50_v = true;
              if ( TrigPath.Contains("HLT_PFHT750_4JetPt50_v") ) trig_bit_PFHT750_4JetPt50_v = true;
              if ( TrigPath.Contains("HLT_PFHT800_4JetPt50_v") ) trig_bit_PFHT800_4JetPt50_v = true;
              if ( TrigPath.Contains("HLT_PFHT850_4JetPt50_v") ) trig_bit_PFHT850_4JetPt50_v = true;
              if ( TrigPath.Contains("HLT_PFJet15_NoCaloMatched_v") ) trig_bit_PFJet15_NoCaloMatched_v = true;
              if ( TrigPath.Contains("HLT_PFJet25_NoCaloMatched_v") ) trig_bit_PFJet25_NoCaloMatched_v = true;
              if ( TrigPath.Contains("HLT_DiPFJet15_NoCaloMatched_v") ) trig_bit_DiPFJet15_NoCaloMatched_v = true;
              if ( TrigPath.Contains("HLT_DiPFJet25_NoCaloMatched_v") ) trig_bit_DiPFJet25_NoCaloMatched_v = true;
              if ( TrigPath.Contains("HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v") ) trig_bit_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v = true;
              if ( TrigPath.Contains("HLT_DiCentralPFJet430_v") ) trig_bit_DiCentralPFJet430_v = true;
              if ( TrigPath.Contains("HLT_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v") ) trig_bit_DoubleJetsC100_DoubleBTagCSV_p026_DoublePFJetsC160_v = true;
              if ( TrigPath.Contains("HLT_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v") ) trig_bit_DoubleJetsC100_DoubleBTagCSV_p014_DoublePFJetsC100MaxDeta1p6_v = true;
              if ( TrigPath.Contains("HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v") ) trig_bit_PFHT650_WideJetMJJ900DEtaJJ1p5_v = true;
              if ( TrigPath.Contains("HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v") ) trig_bit_PFHT650_WideJetMJJ950DEtaJJ1p5_v = true;
              //Calo Jets
              if ( TrigPath.Contains("HLT_CaloJet260_v") ) trig_bit_CaloJet260_v = true;
              if ( TrigPath.Contains("HLT_CaloJet500_NoJetID_v") ) trig_bit_CaloJet500_NoJetID_v = true;
              if ( TrigPath.Contains("HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v") ) trig_bit_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v = true;
              if ( TrigPath.Contains("HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v") ) trig_bit_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v = true;
              if ( TrigPath.Contains("HLT_HT250_CaloMET70_v") ) trig_bit_HT250_CaloMET70_v = true;
	      //EXO-16-003: new physics with multiple displaced jets

              //if ( TrigPath.Contains("HLT_PFMET110_PFMHT110_IDTight_v") ) trig_bit_pfmet110_pfmht110 = true;
              //if ( TrigPath.Contains("HLT_PFMET120_PFMHT120_IDTight_v") ) trig_bit_pfmet120_pfmht120 = true;
              //if ( TrigPath.Contains("HLT_PFMET120_PFMHT120_IDTight_PFHT60_v") ) trig_bit_pfmet120_pfmht120_PFHT60 = true;
              //if ( TrigPath.Contains("HLT_PFMET130_PFMHT130_IDTight_v") ) trig_bit_pfmet130_pfmht130 = true;
              //if ( TrigPath.Contains("HLT_PFMET140_PFMHT140_IDTight_v") ) trig_bit_pfmet140_pfmht140 = true;

              //if ( TrigPath.Contains("HLT_PFMETTypeOne110_PFMHT110_IDTight_v") ) trig_bit_pfmetTypeOne110_pfmht110 = true;
              //if ( TrigPath.Contains("HLT_PFMETTypeOne120_PFMHT120_IDTight_v") ) trig_bit_pfmetTypeOne120_pfmht120 = true;
              //if ( TrigPath.Contains("HLT_PFMETTypeOne120_PFMHT120_IDTight_PFHT60_v") ) trig_bit_pfmetTypeOne120_pfmht120_PFHT60 = true;
              //if ( TrigPath.Contains("HLT_PFMETTypeOne130_PFMHT130_IDTight_v") ) trig_bit_pfmetTypeOne130_pfmht130 = true;
              //if ( TrigPath.Contains("HLT_PFMETTypeOne140_PFMHT140_IDTight_v") ) trig_bit_pfmetTypeOne140_pfmht140 = true;

              //if ( TrigPath.Contains("HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v") ) {
	      //  trig_bit_pfmetnomu110_pfmhtnomu110 = true;
	      //  std::cout << TrigPath << std::endl;
	      //}
              //if ( TrigPath.Contains("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v") ) {
	      //  trig_bit_pfmetnomu120_pfmhtnomu120 = true;
	      //  std::cout << TrigPath << std::endl;
	      //}
              //if ( TrigPath.Contains("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v") ) trig_bit_pfmetnomu120_pfmhtnomu120_PFHT60 = true;
              //if ( TrigPath.Contains("HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v") ) trig_bit_pfmetnomu130_pfmhtnomu130 = true;
              //if ( TrigPath.Contains("HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v") ) trig_bit_pfmetnomu140_pfmhtnomu140 = true;

              //if ( TrigPath.Contains("HLT_Ele27_WPTight_Gsf_v") ) trig_bit_ele27_wptight_gsf = true;
              //if ( TrigPath.Contains("HLT_IsoMu24_v") ) {
	      //  trig_bit_isomu24 = true;
	      //  std::cout << TrigPath << std::endl;
	      //}
           }
        }
    }

    /*
    //MET filters
    edm::Handle<edm::TriggerResults> filterResults; 
    iEvent.getByToken(filterResultsToken, filterResults);

    if( !filterResults.failedToGet() ) { 
        int N_Filters = filterResults->size();
        const edm::TriggerNames & filterName = iEvent.triggerNames(*filterResults);

        for( int i_Trig = 0; i_Trig < N_Filters; ++i_Trig ) { 
	    if (filterResults.product()->accept(i_Trig)) {
	        TString TrigPath =filterName.triggerName(i_Trig);

	        if ( TrigPath.Contains("Flag_HBHENoiseFilter") ) trig_bit_flag_HBHENoiseFilter = true;
	        if ( TrigPath.Contains("Flag_HBHENoiseIsoFilter") ) trig_bit_flag_HBHENoiseIsoFilter = true;
	        if ( TrigPath.Contains("Flag_EcalDeadCellTriggerPrimitiveFilter") ) trig_bit_flag_EcalDeadCellTriggerPrimitiveFilter = true;
	        if ( TrigPath.Contains("Flag_goodVertices") ) trig_bit_flag_goodVertices = true;
	        if ( TrigPath.Contains("Flag_eeBadScFilter") ) trig_bit_flag_eeBadScFilter = true;
	        if ( TrigPath.Contains("Flag_globalSuperTightHalo2016Filter") ) trig_bit_flag_globalSuperTightHalo2016Filter = true;
	    }
        }
    }

    //BadChCand and BadPFMuon filters
    edm::Handle<bool> filterBadChCand; 
    iEvent.getByToken(badChCandFilterToken, filterBadChCand);
    flag_BadChCand = *filterBadChCand;

    edm::Handle<bool> filterBadPFMuon; 
    iEvent.getByToken(badPFMuonFilterToken, filterBadPFMuon);
    flag_BadPFMuon = *filterBadPFMuon;
    */

    //Event info
    isMC = !iEvent.isRealData();
    EventNumber = iEvent.id().event();
    LumiNumber = iEvent.luminosityBlock();
    RunNumber = iEvent.id().run();


    //Initialize met no mu
    float met_pt_nomu_x_L(0.), met_pt_nomu_y_L(0.), met_pt_nomu_x_T(0.), met_pt_nomu_y_T(0.);
    

    //Vertices
    edm::Handle<reco::VertexCollection> VertexColl;
    iEvent.getByToken( vertexToken, VertexColl);
    nPV = VertexColl->size();
    const reco::Vertex* vertex=&VertexColl->front();
    reco::TrackBase::Point vtxPoint(0,0,0);
    if(  VertexColl->size() >= 1 ) {
        vtxPoint = VertexColl->at(0).position();
    }


    /*
    //Loop on MET
    edm::Handle<pat::METCollection> MetColl;
    iEvent.getByToken( metToken, MetColl);
    pat::MET met = MetColl->front();
    met_pt = met.pt();
    met_phi = met.phi();
    met_pt_nomu_x_L = met_pt_nomu_x_T = met.px();//before summing up muons
    met_pt_nomu_y_L = met_pt_nomu_y_T = met.py();//before summing up muons

    //Loop on AK8 jets
    edm::Handle<pat::JetCollection> fatjets;
    iEvent.getByToken( fatjetToken, fatjets );
    //std::vector<pat::Jet> FatJetVect;

    for(std::vector<pat::Jet>::const_iterator it=fatjets->begin(); it!=fatjets->end(); it++) {
        pat::Jet f=*it;
	if ( !isLooseJet(f) ) continue;
	fatjet1_isLoose = true;
        if ( f.pt() < 170 ) continue;
        if ( fabs( f.eta() ) > 2.5 ) continue;
	nLooseFatJets++;
	fatjet1_pt = f.pt();
	if ( !isTightJet(f) ) continue;
	fatjet1_isTight = true;
	nTightFatJets++;
	//FatJetVect.push_back(f);
    }

    */
    //Loop on AK4 jets
    edm::Handle<pat::JetCollection> jets;
    iEvent.getByToken( jetToken, jets );
    std::vector<pat::Jet> JetVect;

    for(std::vector<pat::Jet>::const_iterator it=jets->begin(); it!=jets->end(); it++) {
        pat::Jet j=*it;
	if ( !isLooseJet(j) ) continue;
        if ( j.pt() < 15 ) continue;//this causes a jump at ~30? investigate!
        if ( fabs( j.eta() ) > 5.2 ) continue;
        nLooseJets++;
	if ( isTightJet(j) ) 
	  {
	    nTightJets++;
	  }
	//jet1_pt = j.pt();
	JetVect.push_back(j);
    }

/*
    float m_ht_x(0.), m_ht_y(0.), m_ht_nomu_x_L(0.), m_ht_nomu_y_L(0.), m_ht_nomu_x_T(0.), m_ht_nomu_y_T(0.);
    
    for(unsigned int a=0; a<JetVect.size(); a++){
        m_ht_x -= JetVect.at(a).px();
        m_ht_y -= JetVect.at(a).py();
        m_ht_nomu_x_L -= JetVect.at(a).px();
        m_ht_nomu_y_L -= JetVect.at(a).py();
        m_ht_nomu_x_T -= JetVect.at(a).px();
        m_ht_nomu_y_T -= JetVect.at(a).py();
    }
    
    m_ht = sqrt( pow(m_ht_x,2) + pow(m_ht_y,2)  );
    min_met_mht = std::min(met_pt,m_ht);

    //Loop on muons ---> fix
    edm::Handle<pat::MuonCollection> muons;
    iEvent.getByToken( muonToken, muons );
    //std::vector<pat::Muon> MuonVect;


    //for ( const pat::Muon &m : *muons) {
    for(std::vector<pat::Muon>::const_iterator it=muons->begin(); it!=muons->end(); it++) {
        pat::Muon m=*it;
        //if ( m.pt() < 30 ) continue; //this causes a jump at ~30 GeV, investigate
        if ( fabs( m.eta() ) > 2.4 ) continue; //this selection is necessary
	if (!m.isLooseMuon()) continue;
        muon1_isLoose = true;
	float pfIso04 = (m.pfIsolationR04().sumChargedHadronPt + std::max(m.pfIsolationR04().sumNeutralHadronEt + m.pfIsolationR04().sumPhotonEt - 0.5*m.pfIsolationR04().sumPUPt, 0.) ) / m.pt();
        //if (pfIso04>0.25) continue; //at least loose isolation: try to drop
        met_pt_nomu_x_L += m.px();
        met_pt_nomu_y_L += m.py();
	m_ht_nomu_x_L += m.px();
	m_ht_nomu_y_L += m.py();
	nLooseMuons++;
        //muon1_isLoose = true;
	if (!m.isTightMuon(*vertex)) continue;
        muon1_isTight = true;
        met_pt_nomu_x_T += m.px();
        met_pt_nomu_y_T += m.py();
	m_ht_nomu_x_T += m.px();
	m_ht_nomu_y_T += m.py();
	nTightMuons++;
        //muon1_isTight = true;
 	muon1_pt = m.pt();
        muon1_pfIso04 = pfIso04;
	//MuonVect.push_back(m);
    } // loop over muons, saving only tight muons

    met_pt_nomu_L = sqrt( pow(met_pt_nomu_x_L,2) + pow(met_pt_nomu_y_L,2) );
    met_pt_nomu_T = sqrt( pow(met_pt_nomu_x_T,2) + pow(met_pt_nomu_y_T,2) );
    m_ht_nomu_L = sqrt( pow(m_ht_nomu_x_L,2) + pow(m_ht_nomu_y_L,2)  );
    m_ht_nomu_T = sqrt( pow(m_ht_nomu_x_T,2) + pow(m_ht_nomu_y_T,2)  );
    min_met_mht_nomu_L = std::min(met_pt_nomu_L,m_ht_nomu_L);
    min_met_mht_nomu_T = std::min(met_pt_nomu_T,m_ht_nomu_T);

    
    //Loop on electrons ---> fix, missing Electron IDs
    
    edm::InputTag convLabel = edm::InputTag("reducedEgamma:reducedConversions");
    edm::Handle<reco::ConversionCollection> conversions;
    iEvent.getByLabel( convLabel, conversions );

    //edm::InputTag bsLabel = edm::InputTag("offlineBeamSpot");
    //edm::Handle<reco::BeamSpot> bsHandle;
    //iEvent.getByLabel( bsLabel, bsHandle );
    //const reco::BeamSpot &beamspot = *bsHandle.product();

    edm::Handle<pat::ElectronCollection> electrons;
    iEvent.getByToken( electronToken, electrons );
    //std::vector<pat::Electron> ElectronVect;
    for(std::vector<pat::Electron>::const_iterator it=electrons->begin(); it!=electrons->end(); it++) {
        pat::Electron e=*it;
	///*
	GsfElectron::PflowIsolationVariables pfIso = e.pfIsolationVariables();
	bool isEB = e.isEB() ? true : false;
	float dEtaIn = e.deltaEtaSuperClusterTrackAtVtx();
	float dPhiIn = e.deltaPhiSuperClusterTrackAtVtx();
	float full5x5 = e.full5x5_sigmaIetaIeta();
	float hoe = e.hadronicOverEm();
	float absiso = pfIso.sumChargedHadronPt + max(0.0 , pfIso.sumNeutralHadronEt + pfIso.sumPhotonEt - 0.5 * pfIso.sumPUPt );
	float relIsoWithDBeta_ = absiso/e.pt();
	float ooEmooP_; 
	if( e.ecalEnergy() == 0 ){
	    printf("Electron energy is zero!\n");
	    ooEmooP_ = 999;
	}
        else if( !std::isfinite(e.ecalEnergy())){
	    printf("Electron energy is not finite!\n");
	    ooEmooP_ = 998;
	}
        else{
	    ooEmooP_ = fabs(1.0/e.ecalEnergy() - e.eSuperClusterOverP()/e.ecalEnergy() );
	}
	std::cout << ooEmooP_ << std::endl;
	float d0 = (-1) * e.gsfTrack()->dxy(vtxPoint);
	float dz = e.gsfTrack()->dz(vtxPoint);
	float missHits = e.gsfTrack()->hitPattern().numberOfLostTrackerHits(HitPattern::MISSING_INNER_HITS);
	bool hasMatchConv = ConversionTools::hasMatchedConversion(e, conversions, beamspot.position());
	bool isVeto = passIDWP("VETO",isEB, dEtaIn, dPhiIn, full5x5, hoe, d0, dz, ooEmooP_, hasMatchConv, missHits);
	bool isLoose = passIDWP("LOOSE",isEB, dEtaIn, dPhiIn, full5x5, hoe, d0, dz, ooEmooP_, hasMatchConv, missHits);
	bool isMedium = passIDWP("MEDIUM",isEB, dEtaIn, dPhiIn, full5x5, hoe, d0, dz, ooEmooP_, hasMatchConv, missHits);
	bool isTight = passIDWP("TIGHT",isEB, dEtaIn, dPhiIn, full5x5, hoe, d0, dz, ooEmooP_, hasMatchConv, missHits);
	// Look up the ID decision for this electron in 	
	if ( isLoose ) {
  	    std::cout << "LOOSE ele" << std::endl;
	}
    // */     /*
        if ( e.pt() < 30 ) continue;
        if ( fabs( e.eta() ) > 2.5 ) continue;
	//std::cout << "Electron pt: " << e.pt() << std::endl;
	electron1_pt = e.pt();
	//ElectronVect.push_back(e);
    } // loop over electrons

   */
    
    tree -> Fill();




}


// ------------ method called once each job just before starting event loop  ------------
void 
LongLivedTrigAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
LongLivedTrigAnalyzer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
LongLivedTrigAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}


//Method to define loose jet ID (2016 data)
bool LongLivedTrigAnalyzer::isLooseJet(pat::Jet& jet){
    if(fabs(jet.eta())<=2.7){/// |eta| < 2.7
        if(jet.neutralHadronEnergyFraction()>=0.99) return false;
        if(jet.neutralEmEnergyFraction()>=0.99) return false;
        if((jet.chargedMultiplicity()+jet.neutralMultiplicity())<=1) return false;
            if(fabs(jet.eta())<=2.4) { /// |eta| < 2.4
                if(jet.chargedHadronEnergyFraction()<=0.) return false;
                if(jet.chargedMultiplicity()<=0) return false;
                if(jet.chargedEmEnergyFraction()>=0.99) return false;
            }
    }
    else{ /// |eta| > 2.7
        if(jet.neutralEmEnergyFraction()>=0.90) return false;
        if (fabs(jet.eta())<=3.0) { /// 2.7 < |eta| < 3.0
            if(jet.neutralMultiplicity()<=2) return false;
        }
        else{ /// |eta| > 3.0
           if(jet.neutralMultiplicity()<=10) return false;
        }
    }

    return true;
}

//Method to define tight jet ID (2016 data)
bool LongLivedTrigAnalyzer::isTightJet(pat::Jet& jet){
    if(fabs(jet.eta())<=2.7){/// |eta| < 2.7
        if(jet.neutralHadronEnergyFraction()>=0.90) return false;
        if(jet.neutralEmEnergyFraction()>=0.90) return false;
        if((jet.chargedMultiplicity()+jet.neutralMultiplicity())<=1) return false;
            if(fabs(jet.eta())<=2.4) { /// |eta| < 2.4
                if(jet.chargedHadronEnergyFraction()<=0.) return false;
                if(jet.chargedMultiplicity()<=0) return false;
                if(jet.chargedEmEnergyFraction()>=0.99) return false;
            }
    }
    else{ /// |eta| > 2.7
        if(jet.neutralEmEnergyFraction()>=0.90) return false;
        if (fabs(jet.eta())<=3.0) { /// 2.7 < |eta| < 3.0
            if(jet.neutralMultiplicity()<=2) return false;
        }
        else{ /// |eta| > 3.0
           if(jet.neutralMultiplicity()<=10) return false;
        }
    }

    return true;
}


bool LongLivedTrigAnalyzer::passIDWP(std::string WP, bool isEB, float dEtaIn, float dPhiIn, float full5x5, float hoe, float d0, float dz, float ooemoop, bool conv, int missHits){
  bool pass = false;

  if(WP == "VETO"){
    if(isEB){
      pass = (fabs(dEtaIn) <  0.0126 ) && (fabs(dPhiIn) <  0.107 ) && (full5x5 < 0.012 ) && (hoe <  0.186 ) && (fabs(d0) < 0.0621 ) && (fabs(dz) <  0.613 ) && (fabs(ooemoop) <  0.239 ) && !conv && (missHits <= 2);
    }
    else{
      pass = (fabs(dEtaIn) <  0.0109 ) && (fabs(dPhiIn) <  0.219 ) && (full5x5 < 0.0339 ) && (hoe <  0.0962 ) && (fabs(d0) < 0.279 ) && (fabs(dz) < 0.947 ) && (fabs(ooemoop) < 0.141 ) && !conv && (missHits <= 3);
    }
  }
  if(WP == "LOOSE"){
    if(isEB){
      pass = (fabs(dEtaIn) < 0.00976 ) && (fabs(dPhiIn) < 0.0929 ) && (full5x5 <  0.0105 ) && (hoe < 0.0765 ) && (fabs(d0) < 0.0227 ) && (fabs(dz) < 0.379 ) && (fabs(ooemoop) <  0.184 ) && !conv && (missHits <= 2);
    }
    else{
      pass = (fabs(dEtaIn) < 0.00952 ) && (fabs(dPhiIn) < 0.181 ) && (full5x5 < 0.0318 ) && (hoe < 0.0824 ) && (fabs(d0) < 0.242 ) && (fabs(dz) < 0.921 ) && (fabs(ooemoop) < 0.125 ) && !conv && (missHits <= 1);
    }
  }

  if(WP == "MEDIUM"){
    if(isEB){
      pass = (fabs(dEtaIn) <  0.0094 ) && (fabs(dPhiIn) <  0.0296 ) && (full5x5 <  0.0101 ) && (hoe <  0.0372 ) && (fabs(d0) <  0.0151 ) && (fabs(dz) <  0.238 ) && (fabs(ooemoop) <  0.118 ) && !conv && (missHits <= 2);
    }
    else{
      pass = (fabs(dEtaIn) <  0.00773 ) && (fabs(dPhiIn) <  0.148 ) && (full5x5 <  0.0287 ) && (hoe <  0.0546 ) && (fabs(d0) <  0.0535 ) && (fabs(dz) <  0.572 ) && (fabs(ooemoop) <  0.104 ) && !conv && (missHits <= 1);
    }
  }

  if(WP == "TIGHT"){
    if(isEB){
      pass = (fabs(dEtaIn) <  0.0095 ) && (fabs(dPhiIn) <  0.0291 ) && (full5x5 <  0.0101 ) && (hoe <  0.0372 ) && (fabs(d0) <  0.0144 ) && (fabs(dz) <  0.323 ) && (fabs(ooemoop) <  0.0174 ) && !conv && (missHits <= 2);
    }
    else{
      pass = (fabs(dEtaIn) <  0.00762 ) && (fabs(dPhiIn) <  0.0439 ) && (full5x5 <  0.0287 ) && (hoe <  0.0544 ) && (fabs(d0) <  0.0377 ) && (fabs(dz) <  0.571 ) && (fabs(ooemoop) <  0.01 ) && !conv && (missHits <= 1);
    }
  }
  return pass;
}


//define this as a plug-in
DEFINE_FWK_MODULE(LongLivedTrigAnalyzer);
