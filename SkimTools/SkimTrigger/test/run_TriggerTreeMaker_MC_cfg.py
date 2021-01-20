import FWCore.ParameterSet.Config as cms

process = cms.Process('Tau3MuSkim')

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load("SkimTools.SkimTrigger.Tau3MuTriggerSkimAOD_cff")

#process.GlobalTag.globaltag = '94X_mc2017_realistic_v14'
#process.GlobalTag.globaltag = '102X_upgrade2018_realistic_v20' # run2-2018
process.GlobalTag.globaltag = '112X_mcRun3_2021_realistic_v13' # run3-2021
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
	'root://xrootd-cms.infn.it//store/user/caruta/DsTau3Mu_Run3_GEN-SIM/DsToTauTo3Mu_Run3_112X_mcRun3_2021_realistic_v13-RAW-RECO/201228_140718/0000/DsTau3mu-RAW_step2_1.root', 'root://xrootd-cms.infn.it//store/user/caruta/DsTau3Mu_Run3_GEN-SIM/DsToTauTo3Mu_Run3_112X_mcRun3_2021_realistic_v13-RAW-RECO/201228_140718/0000/DsTau3mu-RAW_step2_101.root', 'root://xrootd-cms.infn.it//store/user/caruta/DsTau3Mu_Run3_GEN-SIM/DsToTauTo3Mu_Run3_112X_mcRun3_2021_realistic_v13-RAW-RECO/201228_140718/0000/DsTau3mu-RAW_step2_102.root'
#	'root://xrootd-cms.infn.it//store/user/caruta/DsTau3Mu_Run3_GEN-SIM/DsToTauTo3Mu_Run3_112X_mcRun3_2021_realistic_v13-AODSIM/201221_211244/0000/DsTau3mu_step2-AODSIM_12.root', 'root://xrootd-cms.infn.it//store/user/caruta/DsTau3Mu_Run3_GEN-SIM/DsToTauTo3Mu_Run3_112X_mcRun3_2021_realistic_v13-AODSIM/201221_211244/0000/DsTau3mu_step2-AODSIM_16.root', 'root://xrootd-cms.infn.it//store/user/caruta/DsTau3Mu_Run3_GEN-SIM/DsToTauTo3Mu_Run3_112X_mcRun3_2021_realistic_v13-AODSIM/201221_211244/0000/DsTau3mu_step2-AODSIM_17.root', 'root://xrootd-cms.infn.it//store/user/caruta/DsTau3Mu_Run3_GEN-SIM/DsToTauTo3Mu_Run3_112X_mcRun3_2021_realistic_v13-AODSIM/201221_211244/0000/DsTau3mu_step2-AODSIM_19.root', 'root://xrootd-cms.infn.it//store/user/caruta/DsTau3Mu_Run3_GEN-SIM/DsToTauTo3Mu_Run3_112X_mcRun3_2021_realistic_v13-AODSIM/201221_211244/0000/DsTau3mu_step2-AODSIM_28.root', 'root://xrootd-cms.infn.it//store/user/caruta/DsTau3Mu_Run3_GEN-SIM/DsToTauTo3Mu_Run3_112X_mcRun3_2021_realistic_v13-AODSIM/201221_211244/0000/DsTau3mu_step2-AODSIM_29.root', 'root://xrootd-cms.infn.it//store/user/caruta/DsTau3Mu_Run3_GEN-SIM/DsToTauTo3Mu_Run3_112X_mcRun3_2021_realistic_v13-AODSIM/201221_211244/0000/DsTau3mu_step2-AODSIM_30.root'
        #'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_1.root','root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_10.root','root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_100.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_101.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_102.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_103.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_104.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_105.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_106.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_107.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_108.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_109.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_11.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_110.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_111.root', 'root://xrootd-cms.infn.it//store/user/caruta/Pythia8_DsTau3Mu_Run3_GEN-SIM/DsTau3Mu_Run3_112X_mcRun3_2021_realistic_v10-AODSIM/201114_085834/0000/TRK-Run3Winter20_20201026_step3-AODSIM_112.root'
	#'root://xrootd-cms.infn.it//store/user/bjoshi/BuTau3Mu/CRAB3_MC2018_BuTau3Mu_13TeV_DIGI/191212_193400/0000/BuTau3Mu_2018MC_106.root',
        #'root://xrootd-cms.infn.it//store/user/wangjian/DsToTau_TauTo3Mu/CRAB3_RunIIAutumn18DR_AODSIM/191120_085131/0000/TSG-RunIIAutumn18DR-00006_99.root',
        # 'root://xrootd-cms.infn.it//store/mc/RunIIFall17DRPremix/DsToTau_To3Mu_MuFilter_TuneCUEP8M1_13TeV-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/70000/FA2225BE-7549-E911-ADE0-3417EBE64BE8.root', 
        #'root://xrootd-cms.infn.it//store/data/Run2018A/DoubleMuonLowMass/AOD/17Sep2018-v1/120000/3C6EECC5-5787-AC43-ACF0-3BE40CE1291C.root',
        #root://xrootd-cms.infn.it//store/data/Run2017F/DoubleMuonLowMass/AOD/09May2018-v1/80000/AECC4C56-BAB0-E811-B92A-008CFA1979AC.root'
        #"file:/lustrehome/venditti/TestMiniAOD2017/CMSSW_9_4_4/src/CrabSubmission/MC/PiGun_RECO.root"
        #"file:/lustre/cms/store/user/rosma/PionGun_Pt0to30GeV/PiGun_13TeV_MC2017_RECO/190313_143541/0000/PiGun_RECO_979.root"
        #'file:/lustre/cms/store/user/fsimone/DsTau3Mu/crab_crab_DsTau3Mu__13TeV_MC2016_RECO/190120_140919/0001/custom_DsTau3Mu_13TeV_RECO_crab350_1010.root',


    )
)


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("Tree_trg.root"))


process.TreeMakerBkg = cms.EDAnalyzer("TriggerAnalysisT3M",
                                      isMcLabel = cms.untracked.bool(True),
                                      isAnaLabel = cms.untracked.bool(True),
                                      muonLabel=cms.InputTag("looseMuons"),
                                      #VertexLabel=cms.InputTag("offlinePrimaryVerticesWithBS"),
                                      VertexLabel=cms.InputTag("offlinePrimaryVertices"),
                                      genParticleLabel=cms.InputTag("genParticles"),
                                      pileupSummary = cms.InputTag("addPileupInfo"),
                                      Cand3MuLabel=cms.InputTag("ThreeMuonsVtxKalmanFit"),
                                      triggerResults = cms.InputTag("TriggerResults", "", "HLT"),
                                      triggerSummary = cms.InputTag("hltTriggerSummaryAOD", "", "HLT"),
                                      AlgInputTag = cms.InputTag( "gtStage2Digis")
				      #gemRecHitTag = cms.untracked.InputTag("gemRecHits")
)




process.TriggerTree = cms.Path(process.ThreeMuonSelSeq*
                              process.TreeMakerBkg
                     )





