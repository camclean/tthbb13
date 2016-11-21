#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <TTree.h>
#include <TH1F.h>
#include <TH2F.h>
#include <sstream>
#include <TFile.h>
#include <TCanvas.h>
#include <TGraph.h>
#include <TGraphErrors.h>
#include <TF1.h>
#include <TROOT.h>
#include <TColor.h>
#include <TRandom3.h>
#include <cmath>
#include "TMath.h"
#include <TSystem.h>
#include <TLorentzVector.h>
#include <TVector3.h>
#include<TProfile.h>
#include<stdio.h>
#include<stdlib.h>
#include<fstream>
#include<TLegend.h>
#include<TStyle.h>
#include<TDirectoryFile.h>

using namespace std;

void matchToGenParticles(string, string, string, bool);

void run(){
  string folder = "root://cmseos.fnal.gov//store/user/camclean/TopTagEfficiency/80X/";
  string qcdFolder = folder + "haddFiles/";
  //--- Function def: 
  //matchToGenParticles(string folder, string input_file, string output_file, bool isSignal)

  matchToGenParticles(folder, "ZprimeToTTJet_M-2000_TuneCUETP8M1_13TeV-amcatnlo-pythia8.root", "ZprimeToTTJet_M-2000_TuneCUETP8M1_13TeV-amcatnlo-pythia8_genMatched.root", 1);
  matchToGenParticles(qcdFolder, "out_0000.root", "qcd_v1_0000.root", 0);
  matchToGenParticles(qcdFolder, "out_0001.root", "qcd_v1_0001.root", 0);
  matchToGenParticles(qcdFolder, "out_0002.root", "qcd_v1_0002.root", 0);
  matchToGenParticles(qcdFolder, "out_0003.root", "qcd_v1_0003.root", 0);
  matchToGenParticles(qcdFolder, "out_0004.root", "qcd_v1_0004.root", 0);
  matchToGenParticles(qcdFolder, "out_0005.root", "qcd_v1_0005.root", 0);
  matchToGenParticles(qcdFolder, "out_0006.root", "qcd_v1_0006.root", 0);
  matchToGenParticles(qcdFolder, "out_0007.root", "qcd_v1_0007.root", 0);
  matchToGenParticles(qcdFolder, "out_0008.root", "qcd_v1_0008.root", 0);
  matchToGenParticles(qcdFolder, "out_0009.root", "qcd_v1_0009.root", 0);
}
float getDeltaR(float genEta, float genPhi, float recoEta, float recoPhi){
  float dphi = abs(genPhi-recoPhi);
  float deta = abs(genEta-recoEta);

  return sqrt(pow(dphi,2) + pow(deta,2));
}
void matchToGenParticles(string input_folder, string input_file, string output_file, bool isSignal){
  string file_name =  input_folder+input_file;
  TFile *F1   = TFile::Open(file_name.c_str() );
  cout << file_name <<endl;

  //Get Tree entries
  std::vector<float> *genInfo_pileup_TrueNumInteractions = 0;
  std::vector<float> *GenParticles_pt = 0;
  std::vector<float> *GenParticles_eta = 0;
  std::vector<float> *GenParticles_phi = 0;
  std::vector<float> *GenParticles_energy = 0;
  std::vector<float> *GenParticles_pdgId = 0;
  std::vector<float> *GenParticles_status = 0;
  std::vector<float> *GenParticles_index = 0;
  std::vector<float> *GenParticles_mother1 = 0;
  std::vector<float> *GenParticles_mother2 = 0;
  std::vector<float> *GenParticles_daughter1 = 0;
  std::vector<float> *GenParticles_daughter2 = 0;

  std::vector<float> *slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_pt = 0;
  std::vector<float> *slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_eta = 0;
  std::vector<float> *slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_phi = 0;
  std::vector<float> *slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_softdropmass = 0;
  std::vector<float> *slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau3 = 0;
  std::vector<float> *slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau2 = 0;
  std::vector<float> *slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau3_groomed = 0;
  std::vector<float> *slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau2_groomed = 0;
  std::vector<float> *patJetsAk8CHSJetsSoftDropPacked_daughters_patJetsAk8CHSJetsSoftDropPacked_daughters_btag_combinedSecondaryVertex = 0;

  TTree *T1    = (TTree*)  F1     ->Get("tree");
  double entries = T1->GetEntries();
  cout<<"entries = "<< entries <<endl;

  T1->SetBranchAddress("genInfo_pileup_TrueNumInteractions", & genInfo_pileup_TrueNumInteractions);
  T1->SetBranchAddress("GenParticles_pt", & GenParticles_pt);
  T1->SetBranchAddress("GenParticles_eta", & GenParticles_eta);
  T1->SetBranchAddress("GenParticles_phi", & GenParticles_phi);
  T1->SetBranchAddress("GenParticles_energy", & GenParticles_energy);
  T1->SetBranchAddress("GenParticles_pdgId", & GenParticles_pdgId);
  T1->SetBranchAddress("GenParticles_status", & GenParticles_status);
  T1->SetBranchAddress("GenParticles_index", & GenParticles_index);
  T1->SetBranchAddress("GenParticles_mother1", & GenParticles_mother1);
  T1->SetBranchAddress("GenParticles_mother2", & GenParticles_mother2);
  T1->SetBranchAddress("GenParticles_daughter1", & GenParticles_daughter1);
  T1->SetBranchAddress("GenParticles_daughter2", & GenParticles_daughter2);

  T1->SetBranchAddress("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_pt", & slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_pt);
  T1->SetBranchAddress("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_eta", & slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_eta);
  T1->SetBranchAddress("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_phi", & slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_phi);
  T1->SetBranchAddress("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_softdropmass", & slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_softdropmass);
  T1->SetBranchAddress("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau3", & slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau3);
  T1->SetBranchAddress("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau2", & slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau2);
  T1->SetBranchAddress("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau3_groomed", & slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau3_groomed);
  T1->SetBranchAddress("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau2_groomed", & slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau2_groomed);
  T1->SetBranchAddress("patJetsAk8CHSJetsSoftDropPacked_daughters_patJetsAk8CHSJetsSoftDropPacked_daughters_btag_combinedSecondaryVertex", & patJetsAk8CHSJetsSoftDropPacked_daughters_patJetsAk8CHSJetsSoftDropPacked_daughters_btag_combinedSecondaryVertex);

  //ignore other branches
  T1->SetBranchStatus("*",0);
  T1->SetBranchStatus("genInfo_pileup_TrueNumInteractions",1);
  T1->SetBranchStatus("GenParticles_pt",1);
  T1->SetBranchStatus("GenParticles_eta",1);
  T1->SetBranchStatus("GenParticles_phi",1);
  T1->SetBranchStatus("GenParticles_energy",1);
  T1->SetBranchStatus("GenParticles_pdgId",1);
  T1->SetBranchStatus("GenParticles_status",1);
  T1->SetBranchStatus("GenParticles_index",1);
  T1->SetBranchStatus("GenParticles_mother1",1);
  T1->SetBranchStatus("GenParticles_mother2",1);
  T1->SetBranchStatus("GenParticles_daughter1",1);
  T1->SetBranchStatus("GenParticles_daughter2",1);

  T1->SetBranchStatus("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_pt",1);
  T1->SetBranchStatus("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_eta",1);
  T1->SetBranchStatus("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_phi",1);
  T1->SetBranchStatus("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_softdropmass",1);
  T1->SetBranchStatus("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau3",1);
  T1->SetBranchStatus("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau2",1);
  T1->SetBranchStatus("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau3_groomed",1);
  T1->SetBranchStatus("slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau2_groomed",1);
  T1->SetBranchStatus("patJetsAk8CHSJetsSoftDropPacked_daughters_patJetsAk8CHSJetsSoftDropPacked_daughters_btag_combinedSecondaryVertex",1);

  //new file
  TFile *outfile = new TFile(output_file.c_str(),"RECREATE");

  //new tree
  //make one entry for each gen particle
  TTree *tree_topTag = new TTree("tree_topTag", "tree_topTag");
  std::map<std::string, float> topTagTreeVars;
  
  //tree variables
  vector <string> listOfVars;
  listOfVars.push_back("npv");
  listOfVars.push_back("pt");
  listOfVars.push_back("eta");
  listOfVars.push_back("phi");
  
  listOfVars.push_back("ak08softdropz10b00_pt");
  listOfVars.push_back("ak08softdropz10b00_eta");
  listOfVars.push_back("ak08softdropz10b00_phi");
  listOfVars.push_back("ak08softdropz10b00_mass");
  listOfVars.push_back("ak08softdropz10b00_tau32");
  listOfVars.push_back("ak08softdropz10b00_tau32_groomed");
  listOfVars.push_back("ak08softdropz10b00_btag");
  listOfVars.push_back("ak08softdropz10b00_deltaRgen");

  for (unsigned i_vars = 0; i_vars < listOfVars.size(); i_vars++){
    topTagTreeVars[ listOfVars[i_vars] ] = -999.99;
    tree_topTag->Branch( (listOfVars[i_vars]).c_str() , &(topTagTreeVars[ listOfVars[i_vars] ]), (listOfVars[i_vars]+"/F").c_str() );
  }

  for (int i=0; i<entries; i++ ){ //entries
    if (i%10000==0) cout<<i<<"  / "<<entries<<endl;

    T1->GetEntry(i);

    //find generator level hadtops or partons and add them to goodGenParticles
    vector <float> goodGenParticles;

    vector <float> genTops;
    vector <float> genTop_daughter1;
    vector <float> genTop_daughter2;
    vector <float> genTop_Wdaughter1;
    vector <float> genTop_Wdaughter2;

    //tops: pdg id = 6; qcd: status = 23 (Pythia 8)
    for (int i_gen=0;i_gen<GenParticles_pt->size();i_gen++){
      if (isSignal && abs(GenParticles_pdgId->at(i_gen))==6){
	genTops.push_back(i_gen);
	genTop_daughter1.push_back(GenParticles_daughter1->at(i_gen));
	genTop_daughter2.push_back(GenParticles_daughter2->at(i_gen));
      }
      else if (!isSignal && GenParticles_status->at(i_gen)==23) goodGenParticles.push_back(i_gen);
    }

    //signal tops
    if (isSignal){
      float daughter1Pos;
      float daughter2Pos;
      float daughter1AbsPdgId;
      float daughter2AbsPdgId;
      
      float Wdaughter1Pos;
      float Wdaughter2Pos;
      float Wdaughter1AbsPdgId;
      float Wdaughter2AbsPdgId;

      //make sure both genTops have a W-daughter (pdg id = +/- 24 and a b-daughter +/- 5
      for (int i_daughter=0; i_daughter< genTop_daughter1.size();i_daughter++){
	daughter1Pos = genTop_daughter1[i_daughter];
	daughter2Pos = genTop_daughter2[i_daughter];
	daughter1AbsPdgId = abs(GenParticles_pdgId->at(daughter1Pos));
	daughter2AbsPdgId = abs(GenParticles_pdgId->at(daughter2Pos));

	if (daughter1AbsPdgId==24 && daughter2AbsPdgId==5){
	  genTop_Wdaughter1.push_back(GenParticles_daughter1->at(daughter1Pos));
	  genTop_Wdaughter2.push_back(GenParticles_daughter2->at(daughter1Pos));
	}
	else if (daughter1AbsPdgId==5 && daughter2AbsPdgId==24){
	  genTop_Wdaughter1.push_back(GenParticles_daughter1->at(daughter2Pos));
	  genTop_Wdaughter2.push_back(GenParticles_daughter2->at(daughter2Pos));
	}
	else{
	  break;
	}
      }
      
      if ((genTop_daughter1.size() != genTop_Wdaughter1.size()) || (genTop_daughter1.size() != genTops.size())) continue;
      
      //save hadtops - check that W does not have a leptonic decay product
      for (int i_Wdaughter=0; i_Wdaughter< genTop_Wdaughter1.size();i_Wdaughter++){
	Wdaughter1Pos = genTop_Wdaughter1[i_Wdaughter];
	Wdaughter2Pos = genTop_Wdaughter2[i_Wdaughter];
	Wdaughter1AbsPdgId = abs(GenParticles_pdgId->at(Wdaughter1Pos));
	Wdaughter2AbsPdgId = abs(GenParticles_pdgId->at(Wdaughter2Pos));
	
	if (Wdaughter1AbsPdgId < 11 && Wdaughter2AbsPdgId < 11) goodGenParticles.push_back(genTops[i_Wdaughter]);
      }
    }

    //match reco particles to gen particles
    //each entry in new tree corresponds to desired gen particle
    int goodGenIndex = -1;
    float genPt = -999;
    float genEta = -999;
    float genPhi = -999;

    for (int i_goodGen=0;i_goodGen<goodGenParticles.size();i_goodGen++){
      goodGenIndex = goodGenParticles[i_goodGen];
      genPt = GenParticles_pt->at(goodGenIndex);
      genEta = GenParticles_eta->at(goodGenIndex);
      genPhi = GenParticles_phi->at(goodGenIndex);

      topTagTreeVars["npv"] = genInfo_pileup_TrueNumInteractions->at(0);
      topTagTreeVars["pt"] = genPt;
      topTagTreeVars["eta"] = genEta;
      topTagTreeVars["phi"] = genPhi;

      //loop over reco particles
      //reco particle is gen-matched if it's closest to the gen particle and deltaR < 0.6
      float minDr = 1000;
      float dR;
      for (int i_sd=0;i_sd<slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_pt->size();i_sd++){
	dR = getDeltaR(genEta,genPhi,slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_eta->at(i_sd),slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_phi->at(i_sd));
	if (dR < minDr){
	  minDr = dR;
	  if (dR < 0.6){
	    topTagTreeVars["ak08softdropz10b00_deltaRgen"] = dR;
	    topTagTreeVars["ak08softdropz10b00_pt"] = slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_pt->at(i_sd);
	    topTagTreeVars["ak08softdropz10b00_eta"] = slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_eta->at(i_sd);
	    topTagTreeVars["ak08softdropz10b00_phi"] = slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_phi->at(i_sd);
	    topTagTreeVars["ak08softdropz10b00_mass"] = slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_softdropmass->at(i_sd);
	    topTagTreeVars["ak08softdropz10b00_tau32"] = slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau3->at(i_sd)/slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau2->at(i_sd);
	    topTagTreeVars["ak08softdropz10b00_tau32_groomed"] = slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau3_groomed->at(i_sd)/slimmedJetsAK8_SoftDrop_slimmedJetsAK8_SoftDrop_tau2_groomed->at(i_sd);
	    //topTagTreeVars["ak08softdropz10b00_btag"] = patJetsAk8CHSJetsSoftDropPacked_daughters_patJetsAk8CHSJetsSoftDropPacked_daughters_btag_combinedSecondaryVertex->at(i_sd);
	  }
	}
      }
      tree_topTag->Fill();
    }
  }

  outfile->cd();
  tree_topTag->Write();
  outfile->Close();
}
