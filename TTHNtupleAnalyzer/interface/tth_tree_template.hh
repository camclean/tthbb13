//Autogenerated using tree_header.jl -> no longer autogenerated, can update manually
#ifndef TTH_TREE
#define TTH_TREE

#include <TTree.h>
#include <string>
#include <map>
#include <cmath>
#include <iostream>

#include "TTH/TTHNtupleAnalyzer/interface/event_interpretation.hh"

#define N_MAX 500
#define M_MAX 100
#define T_MAX 100
#define MET_S_MAX 20

//these are simple 'sentinel values' for uninitialized variables
//for clarity, it would be best to use these instead of manually writing -99 etc.
//this way, undefined variables are always unique and one can write functions to recognize them
#define DEF_VAL_FLOAT -9999.0f
#define DEF_VAL_DOUBLE -9999.0d
#define DEF_VAL_INT -9999
#define FLOAT_EPS 0.0000001f
#define DOUBLE_EPS 0.0000001d

//HEADERGEN_DEFINES

//checks if a branch variable is undefined
inline bool is_undef(int x) { return x==DEF_VAL_INT; };
inline bool is_undef(float x) { return fabs(x-DEF_VAL_FLOAT) < FLOAT_EPS; };
inline bool is_undef(double x) { return fabs(x-DEF_VAL_DOUBLE) < DOUBLE_EPS; };


//macros to initialize 1D and 2D (square) arrays
//x is the array, n is the size, y is the initialized value
#define SET_ZERO(x,n,y) for(int i=0;i<n;i++) {x[i]=y;}
#define SET_ZERO_2(x,n,m,y) for(int i=0;i<n;i++) { for(int j=0;j<m;j++) { x[i][j]=y; } }

/*
This is a simple wrapper class for the TTH-specific flat data format.
To use it, one should load the input file in the standard way using
TFile* f = new TFile("ntuple.root");
TTree* _ttree = (TTree*)f->Get("tthNtupleAnalyzer/events");
and then initialize the class using
TTHTree tree(_ttree);

TTHTree contains the C++ variables for all the branches and functions to conveniently set them.
To attach the branches in the read mode (call SetBranchAddress), call
tree.set_branch_addresses();
outside the event loop.
 You can loop over the events in the standard way

 for (unsigned int i=0; i < _ttree->GetEntries(); i++) {
     tree.loop_initialize(); // <-- this makes sure all the branch variables are cleared from the previous entry
     _ttree->GetEntry(i); // <--- loads the branch contents into the branch variables

     for (int njet=0; njet < tree.n__jet; njet++) {
         float x = tree.jet__pt[njet];
         //do something with the jet pt 
     }
*/
class TTHTree {
public:
	TTHTree(TTree* _tree) { tree = _tree; };
	TTree* tree;
   
        // Helper functions for accessing branches
	template <typename T> 
	T get_address(const std::string name) {
		auto* br = tree->GetBranch(name.c_str());
		if (br==0) {
			std::cerr << "ERROR: get_address TTHTree " << "branch " << name << " does not exist" << std::endl;
			throw std::exception();
		}
		auto* p = br->GetAddress();
		return reinterpret_cast<T>(p);
	}

	double debug__time1c;
	double debug__time1r;
	
	int event__id;
	int event__json;
	int event__lumi;
	int event__run;

	int trigger__bits[T_MAX];
	float trigger__prescale[T_MAX];

	float gen_met__phi;
	float gen_met__pt;
	float gen_met__sumet;

	//top quark in ttbar processes
	//initial top pair decay hypothesis based on leptons
	int hypo1;
	
	//gen-level information from LHE
	float lhe__ht;
	int lhe__n_b;
	int lhe__n_c;
	int lhe__n_e;
	int lhe__n_g;
	float lhe__n_j;
	int lhe__n_l;
	
	int n_sim_b;
	int n_sim_c;

	//MET along with systematic shifts
	float met__phi;
	float met__pt;
	float met__sumet;
	float met__pt__en_down;
	float met__pt__en_up;
	float met__pt__shift[MET_S_MAX];
	float met__px__shift[MET_S_MAX];
	float met__py__shift[MET_S_MAX];
	float met__phi__shift[MET_S_MAX];
    
    int n__met_shift;
    int n__jet;
	int n__lep;

    //number of primary vertices
	int n__pv;
	int n__pvi;

    //number of trigger identifiers
	int n__tr;

	int n__sig_lep;
    
	int pvi__bx[N_MAX];
	float pvi__n0[N_MAX];
	float pvi__ntrue[N_MAX];

	float weight__pu;
	float weight__pu_down;
	float weight__pu_up;
	float weight__trigger;
	float weight__trigger_down;
	float weight__trigger_up;
    
    //HEADERGEN_BRANCH_VARIABLES
    //This comment is for automatic header generation, do not remove

    //initializes all branch variables
	void loop_initialize(void) {
		debug__time1c = DEF_VAL_DOUBLE;
		debug__time1r = DEF_VAL_DOUBLE;
		
		event__id = DEF_VAL_INT;
		event__json = DEF_VAL_INT;
		event__lumi = DEF_VAL_INT;
		event__run = DEF_VAL_INT;
		
		SET_ZERO(trigger__bits, T_MAX, DEF_VAL_INT);
		SET_ZERO(trigger__prescale, T_MAX, DEF_VAL_FLOAT);

		gen_met__phi = DEF_VAL_FLOAT;
		gen_met__pt = DEF_VAL_FLOAT;
		gen_met__sumet = DEF_VAL_FLOAT;

		hypo1 = DEF_VAL_INT;

		lhe__ht = DEF_VAL_FLOAT;
		lhe__n_b = DEF_VAL_INT;
		lhe__n_c = DEF_VAL_INT;
		lhe__n_e = DEF_VAL_INT;
		lhe__n_g = DEF_VAL_INT;
		lhe__n_j = DEF_VAL_FLOAT;
		lhe__n_l = DEF_VAL_INT;
		
		n_sim_b = DEF_VAL_INT;
		n_sim_c = DEF_VAL_INT;
		
		met__phi = DEF_VAL_FLOAT;
		met__pt = DEF_VAL_FLOAT;
		met__sumet = DEF_VAL_FLOAT;
		SET_ZERO(met__pt__shift,  MET_S_MAX, DEF_VAL_FLOAT);
		SET_ZERO(met__px__shift,  MET_S_MAX, DEF_VAL_FLOAT);
		SET_ZERO(met__py__shift,  MET_S_MAX, DEF_VAL_FLOAT);
		SET_ZERO(met__phi__shift, MET_S_MAX, DEF_VAL_FLOAT);
		n__jet = DEF_VAL_INT;
		
		n__lep = DEF_VAL_INT;
		n__tr  = DEF_VAL_INT;
		n__pv  = DEF_VAL_INT;
		n__pvi = DEF_VAL_INT;
        n__met_shift = DEF_VAL_INT;
		n__sig_lep = DEF_VAL_INT;
		SET_ZERO(pvi__bx, N_MAX, DEF_VAL_INT);
		SET_ZERO(pvi__n0, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(pvi__ntrue, N_MAX, DEF_VAL_FLOAT);
		weight__pu = DEF_VAL_FLOAT;
		weight__pu_down = DEF_VAL_FLOAT;
		weight__pu_up = DEF_VAL_FLOAT;
		weight__trigger = DEF_VAL_FLOAT;
		weight__trigger_down = DEF_VAL_FLOAT;
		weight__trigger_up = DEF_VAL_FLOAT;
        
        //HEADERGEN_BRANCH_INITIALIZERS
	}

    //makes branches on a new TTree
	void make_branches(void) {
		tree->Branch("event__id", &event__id, "event__id/I");
		tree->Branch("event__json", &event__json, "event__json/I");
		tree->Branch("event__lumi", &event__lumi, "event__lumi/I");
		tree->Branch("event__run", &event__run, "event__run/I");
		
		tree->Branch("hypo1", &hypo1, "hypo1/I");
		
		tree->Branch("lhe__n_b", &lhe__n_b, "lhe__n_b/I");
		tree->Branch("lhe__n_c", &lhe__n_c, "lhe__n_c/I");
		tree->Branch("lhe__n_e", &lhe__n_e, "lhe__n_e/I");
		tree->Branch("lhe__n_g", &lhe__n_g, "lhe__n_g/I");
		tree->Branch("lhe__n_l", &lhe__n_l, "lhe__n_l/I");
		tree->Branch("n_sim_b", &n_sim_b, "n_sim_b/I");
		tree->Branch("n_sim_c", &n_sim_c, "n_sim_c/I");

		tree->Branch("n__jet", &n__jet, "n__jet/I");
		
		tree->Branch("n__lep", &n__lep, "n__lep/I");
		tree->Branch("n__pv", &n__pv, "n__pv/I");
		tree->Branch("n__pvi", &n__pvi, "n__pvi/I");
		tree->Branch("n__tr", &n__tr, "n__tr/I");
		tree->Branch("n__met_shift", &n__met_shift, "n__met_shift/I");
		tree->Branch("n__sig_lep", &n__sig_lep, "n__sig_lep/I");
		tree->Branch("debug__time1c", &debug__time1c, "debug__time1c/D");
		tree->Branch("debug__time1r", &debug__time1r, "debug__time1r/D");
		tree->Branch("trigger__bits", trigger__bits, "trigger__bits[n__tr]/I");
		tree->Branch("trigger__prescale", trigger__prescale, "trigger__prescale[n__tr]/F");
		tree->Branch("gen_met__phi", &gen_met__phi, "gen_met__phi/F");
		tree->Branch("gen_met__pt", &gen_met__pt, "gen_met__pt/F");
		tree->Branch("gen_met__sumet", &gen_met__sumet, "gen_met__sumet/F");
		
		tree->Branch("lhe__ht", &lhe__ht, "lhe__ht/F");
		tree->Branch("lhe__n_j", &lhe__n_j, "lhe__n_j/F");
		tree->Branch("met__phi", &met__phi, "met__phi/F");
		tree->Branch("met__pt", &met__pt, "met__pt/F");
		tree->Branch("met__sumet", &met__sumet, "met__sumet/F");
		tree->Branch("met__pt__shift", met__pt__shift, "met__pt__shift[n__met_shift]/F");
		tree->Branch("met__px__shift", met__px__shift, "met__px__shift[n__met_shift]/F");
		tree->Branch("met__py__shift", met__py__shift, "met__py__shift[n__met_shift]/F");
		tree->Branch("met__phi__shift", met__phi__shift, "met__phi__shift[n__met_shift]/F");
		tree->Branch("met__pt__en_down", &met__pt__en_down, "met__pt__en_down/F");
		tree->Branch("met__pt__en_up", &met__pt__en_up, "met__pt__en_up/F");
		tree->Branch("pvi__bx", pvi__bx, "pvi__bx[n__pvi]/I");
		tree->Branch("pvi__n0", pvi__n0, "pvi__n0[n__pvi]/F");
		tree->Branch("pvi__ntrue", pvi__ntrue, "pvi__ntrue[n__pvi]/F");
		tree->Branch("weight__pu", &weight__pu, "weight__pu/F");
		tree->Branch("weight__pu_down", &weight__pu_down, "weight__pu_down/F");
		tree->Branch("weight__pu_up", &weight__pu_up, "weight__pu_up/F");
		tree->Branch("weight__trigger", &weight__trigger, "weight__trigger/F");
		tree->Branch("weight__trigger_down", &weight__trigger_down, "weight__trigger_down/F");
		tree->Branch("weight__trigger_up", &weight__trigger_up, "weight__trigger_up/F");
        
        //HEADERGEN_BRANCH_CREATOR
	}

    //connects the branches of an existing TTree to variables
    //used when loading the file
	void set_branch_addresses(void) {
		tree->SetBranchAddress("debug__time1c", &debug__time1c);
		tree->SetBranchAddress("debug__time1r", &debug__time1r);
		tree->SetBranchAddress("event__id", &event__id);
		tree->SetBranchAddress("event__json", &event__json);
		tree->SetBranchAddress("event__lumi", &event__lumi);
		tree->SetBranchAddress("event__run", &event__run);
		tree->SetBranchAddress("gen_met__phi", &gen_met__phi);
		tree->SetBranchAddress("gen_met__pt", &gen_met__pt);
		tree->SetBranchAddress("gen_met__sumet", &gen_met__sumet);
		
		tree->SetBranchAddress("hypo1", &hypo1);
		
		tree->SetBranchAddress("lhe__ht", &lhe__ht);
		tree->SetBranchAddress("lhe__n_b", &lhe__n_b);
		tree->SetBranchAddress("lhe__n_c", &lhe__n_c);
		tree->SetBranchAddress("lhe__n_e", &lhe__n_e);
		tree->SetBranchAddress("lhe__n_g", &lhe__n_g);
		tree->SetBranchAddress("lhe__n_j", &lhe__n_j);
		tree->SetBranchAddress("lhe__n_l", &lhe__n_l);
		tree->SetBranchAddress("n_sim_b", &n_sim_b);
		tree->SetBranchAddress("n_sim_c", &n_sim_c);
		
		tree->SetBranchAddress("met__phi", &met__phi);
		tree->SetBranchAddress("met__pt", &met__pt);
		tree->SetBranchAddress("met__sumet", &met__sumet);
		tree->SetBranchAddress("met__pt__en_down", &met__pt__en_down);
		tree->SetBranchAddress("met__pt__en_up", &met__pt__en_up);
		tree->SetBranchAddress("n__jet", &n__jet);
		tree->SetBranchAddress("n__lep", &n__lep);
		tree->SetBranchAddress("n__pv", &n__pv);
		tree->SetBranchAddress("n__pvi", &n__pvi);
		tree->SetBranchAddress("n__sig_lep", &n__sig_lep);
		tree->SetBranchAddress("pvi__bx", pvi__bx);
		tree->SetBranchAddress("pvi__n0", pvi__n0);
		tree->SetBranchAddress("pvi__ntrue", pvi__ntrue);
		tree->SetBranchAddress("weight__pu", &weight__pu);
		tree->SetBranchAddress("weight__pu_down", &weight__pu_down);
		tree->SetBranchAddress("weight__pu_up", &weight__pu_up);
		tree->SetBranchAddress("weight__trigger", &weight__trigger);
		tree->SetBranchAddress("weight__trigger_down", &weight__trigger_down);
		tree->SetBranchAddress("weight__trigger_up", &weight__trigger_up);
        
        //HEADERGEN_BRANCH_SETADDRESS

	}
	
	Event* as_event() {
		std::vector<Particle*> particles;
		std::vector<Particle*> jets;
		std::vector<Particle*> gen_jets;
		std::vector<Particle*> top_decay;
		std::vector<Particle*> higgs_decay;
		std::vector<Particle*> leptons;
		std::vector<Particle*> gen_leptons;
		
		for (int i=0;i < n__jet; i++) {
			Particle* jet = new Particle(jet__pt[i], jet__eta[i], jet__phi[i], jet__mass[i], jet__id[i], i);
			particles.push_back(jet);
			jets.push_back(jet);
		}
		
		for (int i=0;i < n__jet; i++) {
			Particle* jet = new Particle(gen_jet__pt[i], gen_jet__eta[i], gen_jet__phi[i], gen_jet__mass[i], gen_jet__id[i], i);
			particles.push_back(jet);
			gen_jets.push_back(jet);
		}
		
		for (int i=0;i < n__lep; i++) {
			Particle* lep = new Particle(lep__pt[i], lep__eta[i], lep__phi[i], lep__mass[i], lep__id[i], i);
			particles.push_back(lep);
			leptons.push_back(lep);
		}
		
		for (int i=0;i < n__lep; i++) {
			Particle* lep = new Particle(gen_lep__pt[i], gen_lep__eta[i], gen_lep__phi[i], gen_lep__mass[i], gen_lep__id[i], i);
			particles.push_back(lep);
			gen_leptons.push_back(lep);
		}
		
		Particle* d1 = new Particle(gen_t__w_d1__pt, gen_t__w_d1__eta, gen_t__w_d1__phi, gen_t__w_d1__mass, gen_t__w_d1__id);
		top_decay.push_back(d1);
		particles.push_back(d1);
		
		Particle* d2 = new Particle(gen_t__w_d2__pt, gen_t__w_d2__eta, gen_t__w_d2__phi, gen_t__w_d2__mass, gen_t__w_d2__id);
		top_decay.push_back(d2);
		particles.push_back(d2);
		;
		Particle* d3 = new Particle(gen_tbar__w_d1__pt, gen_tbar__w_d1__eta, gen_tbar__w_d1__phi, gen_tbar__w_d1__mass, gen_tbar__w_d1__id);
		top_decay.push_back(d3);
		particles.push_back(d3);
		
		Particle* d4 = new Particle(gen_tbar__w_d2__pt, gen_tbar__w_d2__eta, gen_tbar__w_d2__phi, gen_tbar__w_d2__mass, gen_tbar__w_d2__id);
		top_decay.push_back(d4);
		particles.push_back(d4);
		
		Particle* d5 = new Particle(gen_t__b__pt, gen_t__b__eta, gen_t__b__phi, gen_t__b__mass, 5);
		top_decay.push_back(d5);
		particles.push_back(d5);
		
		Particle* d6 = new Particle(gen_tbar__b__pt, gen_tbar__b__eta, gen_tbar__b__phi, gen_tbar__b__mass, -5);
		top_decay.push_back(d6);
		particles.push_back(d6);
		
		Particle* d7 = new Particle(gen_b__pt, gen_b__eta, gen_b__phi, gen_b__mass, 5);
		higgs_decay.push_back(d7);
		particles.push_back(d7);
		
		Particle* d8 = new Particle(gen_bbar__pt, gen_bbar__eta, gen_bbar__phi, gen_bbar__mass, -5);
		higgs_decay.push_back(d8);
		particles.push_back(d8);
		
		return new Event(particles, jets, gen_jets, leptons, gen_leptons, top_decay, higgs_decay);
	}
};

#endif
