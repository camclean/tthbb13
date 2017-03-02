//root -l -b plotWPeff.C

#include <cstdlib>
#include "TClonesArray.h"
#include "TLorentzVector.h"
#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
#include "TFile.h"
#include "TF1.h"
#include <iostream>
#include <fstream>
#include <ostream>
#include "TChain.h"
#include "TLatex.h"
#include "THStack.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TColor.h"
#include "TStyle.h"
#include "TPaveLabel.h"
#include "TPaveText.h"
#include "TString.h"
#include <vector>
#include <algorithm>
#include "TROOT.h"
// #include "CMS_lumi.C"

void plotEff(string, string, string, float, float, float, string);

void plotWPeff(){
  //function definitions: 
  //plotEff(string sigFile, string WPpaveLabel, string WPfileLabel, float 74X_SD_tau32cut, float 76X_SD_tau32cut, float 76X_PUPPI_SD_tau32cut, string date)

  string date = "20170220";
  plotEff("root://cmseos.fnal.gov//store/user/camclean/TopTagEfficiency/80X/v1/Zprime/ZPN_2000.root", "0.1%", "0p1", 0.44, 0.5, 0.46, date);
  plotEff("root://cmseos.fnal.gov//store/user/camclean/TopTagEfficiency/80X/v1/Zprime/ZPN_2000.root", "0.3%", "0p3", 0.5, 0.57, 0.54, date);
  plotEff("root://cmseos.fnal.gov//store/user/camclean/TopTagEfficiency/80X/v1/Zprime/ZPN_2000.root", "1%", "1p0", 0.59, 0.67, 0.65, date);
  plotEff("root://cmseos.fnal.gov//store/user/camclean/TopTagEfficiency/80X/v1/Zprime/ZPN_2000.root", "3%", "3p0", 0.69, 0.81, 0.46, date);
}
void plotEff(string SigFile, string WPpaveLabel, string WPfileLabel, float SD_tau32cut_74X, float SD_tau32cut_76X, float PUPPI_SD_tau32cut_76X, string date){
  gStyle->SetOptStat(0);
  gROOT->UseCurrentStyle();
  gROOT->ForceStyle();
  gROOT->Reset();
  gROOT->ForceStyle(); 

  cout<<"opening "<<SigFile<<endl;
  TFile * F_sig =  TFile::Open( SigFile.c_str());

  // Get Tree entries
  std::vector<float> *true_top_pt = 0;
  std::vector<float> *true_top_eta = 0;
  std::vector<float> *true_top_npv = 0;

  std::vector<float> *true_top_AK8_CHS_SoftDrop_softdropmass = 0;
  std::vector<float> *true_top_AK8_CHS_SoftDrop_tau3 = 0;
  std::vector<float> *true_top_AK8_CHS_SoftDrop_tau2 = 0;
  std::vector<float> *true_top_AK8_PUPPI_SoftDrop_softdropmass = 0;
  std::vector<float> *true_top_AK8_PUPPI_SoftDrop_tau3 = 0;
  std::vector<float> *true_top_AK8_PUPPI_SoftDrop_tau2 = 0;

  TTree *T_sig    = (TTree*)  F_sig     ->Get("tree");

  double treeNentries = T_sig->GetEntries();
  cout<<"treeNentries = "<< treeNentries <<endl;

  //Get desired branches
  T_sig->SetBranchAddress("true_top_pt", & true_top_pt);
  T_sig->SetBranchAddress("true_top_eta", & true_top_eta);
  T_sig->SetBranchAddress("true_top_npv", & true_top_npv);

  T_sig->SetBranchAddress("true_top_AK8_CHS_SoftDrop_softdropmass", & true_top_AK8_CHS_SoftDrop_softdropmass);
  T_sig->SetBranchAddress("true_top_AK8_CHS_SoftDrop_tau3", & true_top_AK8_CHS_SoftDrop_tau3);
  T_sig->SetBranchAddress("true_top_AK8_CHS_SoftDrop_tau2", & true_top_AK8_CHS_SoftDrop_tau2);
  T_sig->SetBranchAddress("true_top_AK8_PUPPI_SoftDrop_softdropmass", & true_top_AK8_PUPPI_SoftDrop_softdropmass);
  T_sig->SetBranchAddress("true_top_AK8_PUPPI_SoftDrop_tau3", & true_top_AK8_PUPPI_SoftDrop_tau3);
  T_sig->SetBranchAddress("true_top_AK8_PUPPI_SoftDrop_tau2", & true_top_AK8_PUPPI_SoftDrop_tau2);

  //ignoring all other branches
  T_sig->SetBranchStatus("*",0);
  T_sig->SetBranchStatus("true_top_pt",1);
  T_sig->SetBranchStatus("true_top_eta",1);
  T_sig->SetBranchStatus("true_top_npv",1);

  T_sig->SetBranchStatus("true_top_AK8_CHS_SoftDrop_softdropmass",1);
  T_sig->SetBranchStatus("true_top_AK8_CHS_SoftDrop_tau3",1);
  T_sig->SetBranchStatus("true_top_AK8_CHS_SoftDrop_tau2",1);
  T_sig->SetBranchStatus("true_top_AK8_PUPPI_SoftDrop_softdropmass",1);
  T_sig->SetBranchStatus("true_top_AK8_PUPPI_SoftDrop_tau3",1);
  T_sig->SetBranchStatus("true_top_AK8_PUPPI_SoftDrop_tau2",1);

  //ZPN 2000 histograms
  vector<string> xAxisLabels;
  vector<string> xAxisVars;
  vector<int> nBinsX;
  vector<float> x_min;
  vector<float> x_max;

  vector<string> WPlabel;
  vector<string> WPlegLabel;
  vector<Color_t> histColorVec;

  //x-axis variables
  xAxisLabels.push_back("Parton p_{T}"); xAxisVars.push_back("pt"); nBinsX.push_back(5); x_min.push_back(800.); x_max.push_back(1000.);
  xAxisLabels.push_back("Parton #eta"); xAxisVars.push_back("eta"); nBinsX.push_back(45); x_min.push_back(-2.25); x_max.push_back(2.25);
  xAxisLabels.push_back("Number of Pileup Vertices"); xAxisVars.push_back("npv"); nBinsX.push_back(40); x_min.push_back(0.); x_max.push_back(40.);

  WPlabel.push_back(Form("WP_bg%s_SD_74X",WPfileLabel.c_str())); WPlegLabel.push_back("74X m_{SD} + #tau_{32} WP"); histColorVec.push_back(kRed);
  WPlabel.push_back(Form("WP_bg%s_SD_76X",WPfileLabel.c_str())); WPlegLabel.push_back("76X m_{SD} + #tau_{32} WP"); histColorVec.push_back(kBlue);
  WPlabel.push_back(Form("WP_bg%s_PUPPISD_76X",WPfileLabel.c_str())); WPlegLabel.push_back("76X PUPPI m_{SD} + #tau_{32} WP"); histColorVec.push_back(kGreen+1);

  //denominator histograms
  TH1D *histos_denom[xAxisLabels.size()][WPlabel.size()];
  
  //numerator histograms
  TH1D *histos_num[xAxisLabels.size()][WPlabel.size()];

  //naming histograms
  for (unsigned int i_xAxisLabels=0; i_xAxisLabels<xAxisLabels.size(); i_xAxisLabels++){
    for (unsigned int i_WPlabel=0; i_WPlabel<WPlabel.size(); i_WPlabel++){
      histos_denom[i_xAxisLabels][i_WPlabel] = new TH1D(Form("h_denom_%s_%s",WPlabel[i_WPlabel].c_str(),xAxisVars[i_xAxisLabels].c_str()),Form(";TaggingEfficiency,%s",xAxisLabels[i_xAxisLabels].c_str()),nBinsX[i_xAxisLabels],x_min[i_xAxisLabels],x_max[i_xAxisLabels]);
      histos_num[i_xAxisLabels][i_WPlabel] = new TH1D(Form("h_num_%s_%s",WPlabel[i_WPlabel].c_str(),xAxisVars[i_xAxisLabels].c_str()),Form(";TaggingEfficiency,%s",xAxisLabels[i_xAxisLabels].c_str()),nBinsX[i_xAxisLabels],x_min[i_xAxisLabels],x_max[i_xAxisLabels]);
    }
  }

  //filling histograms
  for (int i=0; i<treeNentries; i++ ){ //entries
    if (i%10000==0) cout<<i<<"  / "<<treeNentries<<endl;

    T_sig->GetEntry(i);

    //considering matched gen-tops
    if(true_top_pt->size()>0){ 
      float AK8_CHS_SoftDrop_tau32 = true_top_AK8_CHS_SoftDrop_tau3->at(0)/true_top_AK8_CHS_SoftDrop_tau2->at(0);//ungroomed tau32 from softdrop jet collection
      float AK8_PUPPI_SoftDrop_tau32 = true_top_AK8_PUPPI_SoftDrop_tau3->at(0)/true_top_AK8_PUPPI_SoftDrop_tau2->at(0);//ungroomed tau32 from PUPPI softdrop jet collection

      //fiducial cut: require tau32 > 0.0
      bool tau32_pass_74X = AK8_CHS_SoftDrop_tau32 > 0.0;
      bool tau32_pass_76X = AK8_CHS_SoftDrop_tau32 > 0.0;
      bool PUPPI_tau32_pass_76X = AK8_PUPPI_SoftDrop_tau32 > 0.0;

      //top-tagging cuts
      bool SD_tau32_pass_74X = (true_top_AK8_CHS_SoftDrop_softdropmass->at(0) > 110) && (true_top_AK8_CHS_SoftDrop_softdropmass->at(0) < 210.) && (AK8_CHS_SoftDrop_tau32 < SD_tau32cut_74X);
      bool SD_tau32_pass_76X = (true_top_AK8_CHS_SoftDrop_softdropmass->at(0) > 105.) && (true_top_AK8_CHS_SoftDrop_softdropmass->at(0) < 220.) && (AK8_CHS_SoftDrop_tau32 < SD_tau32cut_76X);
      bool PUPPI_SD_tau32_pass_76X = (true_top_AK8_PUPPI_SoftDrop_softdropmass->at(0) > 105.) && (true_top_AK8_PUPPI_SoftDrop_softdropmass->at(0) < 210.) && (AK8_PUPPI_SoftDrop_tau32 < PUPPI_SD_tau32cut_76X);

      vector<float> xAxisVars;
      vector<bool> numCutBools;
      vector<bool> fiducialCutBools;
      
      xAxisVars.push_back(true_top_pt->at(0));
      xAxisVars.push_back(true_top_eta->at(0));
      xAxisVars.push_back(true_top_npv->at(0));
    
      numCutBools.push_back(SD_tau32_pass_74X); fiducialCutBools.push_back(tau32_pass_74X); 
      numCutBools.push_back(SD_tau32_pass_76X); fiducialCutBools.push_back(tau32_pass_76X);
      numCutBools.push_back(PUPPI_SD_tau32_pass_76X); fiducialCutBools.push_back(PUPPI_tau32_pass_76X);

    
      for (unsigned int i_numCutBools=0; i_numCutBools<numCutBools.size(); i_numCutBools++){
	if (fiducialCutBools[i_numCutBools]){
	  for (unsigned int i_xAxisVars=0; i_xAxisVars<xAxisVars.size(); i_xAxisVars++){
	    histos_denom[i_xAxisVars][i_numCutBools]->Fill(xAxisVars[i_xAxisVars]);
	    if (numCutBools[i_numCutBools]) histos_num[i_xAxisVars][i_numCutBools]->Fill(xAxisVars[i_xAxisVars]);
	  }//loop over x-axis variables
	}//fiducial cut requirement
      }//loop over working points
    }//end gen-top if statement
  }//end event loop

  //plotting histograms
  for (unsigned int i_xAxisLabels=0; i_xAxisLabels<xAxisLabels.size(); i_xAxisLabels++){
    TCanvas *c1237= new TCanvas("c1237","",1,1,745,640);

    // TCanvas *c1 = new TCanvas("c1", "c1",1,1,745,701);
    gStyle->SetOptFit(1);
    gStyle->SetOptStat(0);
    c1237->SetHighLightColor(2);
    c1237->Range(0,0,1,1);
    c1237->SetFillColor(0);
    c1237->SetBorderMode(0);
    c1237->SetBorderSize(2);
    c1237->SetTickx(1);
    c1237->SetTicky(1);
    c1237->SetLeftMargin(0.14);
    c1237->SetRightMargin(0.04);
    c1237->SetTopMargin(0.08);
    c1237->SetBottomMargin(0.15);
    c1237->SetFrameFillStyle(0);
    c1237->SetFrameBorderMode(0);

    TLegend * leg;
    leg = new TLegend( 0.54, 0.18,0.58, 0.58); //0.51, 0.66,0.84, 0.83
    leg->SetBorderSize(0);
    leg->SetFillColor(0);
    leg->SetFillStyle(4000);
    leg->SetTextSize(0.032);      
    
    for (unsigned int i_WPlabel=0; i_WPlabel<WPlabel.size(); i_WPlabel++){
      histos_denom[i_xAxisLabels][i_WPlabel]->Sumw2();
      histos_num[i_xAxisLabels][i_WPlabel]->Sumw2();
      histos_num[i_xAxisLabels][i_WPlabel]->Divide(histos_num[i_xAxisLabels][i_WPlabel],histos_denom[i_xAxisLabels][i_WPlabel], 1, 1, "B");

      histos_num[i_xAxisLabels][i_WPlabel]->GetXaxis()->SetNoExponent();
      histos_num[i_xAxisLabels][i_WPlabel]->GetXaxis()->SetMoreLogLabels();

      histos_num[i_xAxisLabels][i_WPlabel]->GetXaxis()->SetTitleOffset(1.15);
      histos_num[i_xAxisLabels][i_WPlabel]->GetXaxis()->SetTitleFont(42);

      histos_num[i_xAxisLabels][i_WPlabel]->GetYaxis()->SetTitleOffset(1.17);
      histos_num[i_xAxisLabels][i_WPlabel]->GetYaxis()->SetTitleFont(42);
      //histos_num[i_xAxisLabels][i_WPlabel]->GetYaxis()->SetRangeUser(0,1.25);

      histos_num[i_xAxisLabels][i_WPlabel]->SetLineWidth(2);
      histos_num[i_xAxisLabels][i_WPlabel]->SetLineColor(histColorVec[i_WPlabel]);

      if (i_WPlabel==0) histos_num[i_xAxisLabels][i_WPlabel]->Draw("EP");
      else histos_num[i_xAxisLabels][i_WPlabel]->Draw("EPSAME");

      leg->AddEntry( histos_num[i_xAxisLabels][i_WPlabel]   , WPlegLabel[i_WPlabel].c_str() , "LP" );
    }

    leg->Draw("same");
    
    TLatex *   tex = new TLatex(0.18,0.83,"#font[62]{CMS} #font[52]{Simulation Preliminary}");
    tex->SetNDC();
    tex->SetTextFont(42);
    tex->SetTextSize(0.0625);
    tex->SetLineWidth(2);
    tex->Draw();

    tex = new TLatex(0.57,0.87, Form("#splitline{Z'#rightarrowt#bar{t}, M_{Z'} = 2 TeV}{#varepsilon_{B} = %s}",WPpaveLabel.c_str()));
    tex->SetNDC();
    tex->SetTextAlign(13);
    tex->SetTextFont(42);
    tex->SetTextSize(0.032);
    tex->SetLineWidth(2);
    tex->Draw();
	
    gPad->RedrawAxis();
	
    string savename = "effPlots/80Xv1/OldWPeffvs" + xAxisVars[i_xAxisLabels] + "_WP_bg" + WPfileLabel + "_" + date;
    c1237->SaveAs(Form("%s.pdf",savename.c_str()));    
    c1237->SaveAs(Form("%s.root",savename.c_str()));    
  }
}


