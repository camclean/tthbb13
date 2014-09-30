//Autogenerated
#include <TTree.h>
#include <string>
#include <map>
#define N_MAX 500
#define M_MAX 100
//these are simple 'sentinel values' for uninitialized variables
#define DEF_VAL_FLOAT -9999.0f
#define DEF_VAL_DOUBLE -9999.0d
#define DEF_VAL_INT -9999
#define FLOAT_EPS 0.0000001f
#define DOUBLE_EPS 0.0000001d
constexpr bool is_undef(int x) { return x==DEF_VAL_INT; };
constexpr bool is_undef(float x) { return fabs(x-DEF_VAL_FLOAT) < FLOAT_EPS; };
constexpr bool is_undef(double x) { return fabs(x-DEF_VAL_DOUBLE) < DOUBLE_EPS; };
#define SET_ZERO(x,n,y) for(int i=0;i<n;i++) {x[i]=y;}
#define SET_ZERO_2(x,n,y) for(int i=0;i<n;i++) { for(int j=0;j<n;j++) { x[i][j]=y; } }
class TTHTree {
public:
	TTHTree(TTree* _tree);
	TTree* tree;
	std::map<const std::string, const void*> branch_map;
	double debug__time1c;
	double debug__time1r;
	int event__id;
	int event__json;
	int event__lumi;
	int event__run;
	float gen_jet__eta[N_MAX];
	int gen_jet__id[N_MAX];
	float gen_jet__mass[N_MAX];
	float gen_jet__phi[N_MAX];
	float gen_jet__pt[N_MAX];
	int gen_jet__status[N_MAX];
	float gen_jet_parton__eta[N_MAX];
	int gen_jet_parton__id[N_MAX];
	float gen_jet_parton__mass[N_MAX];
	float gen_jet_parton__phi[N_MAX];
	float gen_jet_parton__pt[N_MAX];
	int gen_jet_parton__status[N_MAX];
	float gen_lep__eta[N_MAX];
	int gen_lep__id[N_MAX];
	float gen_lep__mass[N_MAX];
	float gen_lep__phi[N_MAX];
	float gen_lep__pt[N_MAX];
	int gen_lep__status[N_MAX];
	float gen_met__phi;
	float gen_met__pt;
	float jet__bd_csv[N_MAX];
	float jet__ce_e[N_MAX];
	float jet__ch_e[N_MAX];
	float jet__el_e[N_MAX];
	float jet__energy[N_MAX];
	float jet__eta[N_MAX];
	int jet__id[N_MAX];
	float jet__pileupJetId[N_MAX];
	float jet__mass[N_MAX];
	float jet__mu_e[N_MAX];
	float jet__ne_e[N_MAX];
	float jet__nh_e[N_MAX];
	float jet__ph_e[N_MAX];
	float jet__phi[N_MAX];
	float jet__pt[N_MAX];
        float jet__vtxMass[N_MAX];
        int   jet__vtxNtracks[N_MAX];
        float jet__vtx3DVal[N_MAX];
        float jet__vtx3DSig[N_MAX];
	float jet_toptagger__energy[N_MAX];
	float jet_toptagger__eta[N_MAX];
	float jet_toptagger__mass[N_MAX];
	float jet_toptagger__min_mass[N_MAX];
	int jet_toptagger__n_sj[N_MAX];
	float jet_toptagger__phi[N_MAX];
	float jet_toptagger__pt[N_MAX];
	float jet_toptagger__top_mass[N_MAX];
	float jet_toptagger__w_mass[N_MAX];
	float jet_toptagger_sj__energy[N_MAX];
	float jet_toptagger_sj__eta[N_MAX];
	float jet_toptagger_sj__mass[N_MAX];
	float jet_toptagger_sj__phi[N_MAX];
	float jet_toptagger_sj__pt[N_MAX];
	float lep__ch_iso[N_MAX];
	int lep__charge[N_MAX];
	float lep__dxy[N_MAX];
	float lep__dz[N_MAX];
	float lep__ec_iso[N_MAX];
	float lep__eta[N_MAX];
	float lep__hc_iso[N_MAX];
	int lep__id[N_MAX];
	int lep__id_bitmask[N_MAX];
	int lep__is_loose[N_MAX];
	int lep__is_medium[N_MAX];
	int lep__is_tight[N_MAX];
	float lep__mass[N_MAX];
	float lep__mva[N_MAX];
	float lep__p_iso[N_MAX];
	float lep__ph_iso[N_MAX];
	float lep__phi[N_MAX];
	float lep__pt[N_MAX];
	float lep__puch_iso[N_MAX];
	float lep__rel_iso[N_MAX];
	float lhe__ht;
	int lhe__n_b;
	int lhe__n_c;
	int lhe__n_e;
	int lhe__n_g;
	float lhe__n_j;
	int lhe__n_l;
	float met__phi;
	float met__pt;
	float met__pt__en_down;
	float met__pt__en_up;
	int n__jet;
	int n__jet_toptagger;
	int n__jet_toptagger_sj;
	int n__lep;
	int n__pv;
	int n__pvi;
	int pvi__bx[N_MAX];
	float pvi__n0[N_MAX];
	float pvi__ntrue[N_MAX];
	float weight__pu;
	float weight__pu__up;
	float weight__pu_down;
	float weight__trigger;
	float weight__trigger_down;
	float weight__trigger_up;
	void loop_initialize(void) {
		debug__time1c = DEF_VAL_DOUBLE;
		debug__time1r = DEF_VAL_DOUBLE;
		event__id = DEF_VAL_INT;
		event__json = DEF_VAL_INT;
		event__lumi = DEF_VAL_INT;
		event__run = DEF_VAL_INT;
		SET_ZERO(gen_jet__eta, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(gen_jet__id, N_MAX, DEF_VAL_INT);
		SET_ZERO(gen_jet__mass, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(gen_jet__phi, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(gen_jet__pt, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(gen_jet__status, N_MAX, DEF_VAL_INT);
		SET_ZERO(gen_jet_parton__eta, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(gen_jet_parton__id, N_MAX, DEF_VAL_INT);
		SET_ZERO(gen_jet_parton__mass, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(gen_jet_parton__phi, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(gen_jet_parton__pt, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(gen_jet_parton__status, N_MAX, DEF_VAL_INT);
		SET_ZERO(gen_lep__eta, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(gen_lep__id, N_MAX, DEF_VAL_INT);
		SET_ZERO(gen_lep__mass, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(gen_lep__phi, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(gen_lep__pt, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(gen_lep__status, N_MAX, DEF_VAL_INT);
		gen_met__phi = DEF_VAL_FLOAT;
		gen_met__pt = DEF_VAL_FLOAT;
		SET_ZERO(jet__bd_csv, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__ce_e, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__ch_e, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__el_e, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__energy, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__eta, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__id, N_MAX, DEF_VAL_INT);
		SET_ZERO(jet__pileupJetId, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__mass, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__mu_e, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__ne_e, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__nh_e, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__ph_e, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__phi, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__pt, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__vtxMass, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__vtxNtracks, N_MAX, DEF_VAL_INT);
		SET_ZERO(jet__vtx3DVal, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet__vtx3DSig, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger__energy, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger__eta, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger__mass, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger__min_mass, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger__n_sj, N_MAX, DEF_VAL_INT);
		SET_ZERO(jet_toptagger__phi, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger__pt, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger__top_mass, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger__w_mass, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger_sj__energy, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger_sj__eta, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger_sj__mass, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger_sj__phi, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(jet_toptagger_sj__pt, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__ch_iso, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__charge, N_MAX, DEF_VAL_INT);
		SET_ZERO(lep__dxy, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__dz, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__ec_iso, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__eta, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__hc_iso, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__id, N_MAX, DEF_VAL_INT);
		SET_ZERO(lep__id_bitmask, N_MAX, DEF_VAL_INT);
		SET_ZERO(lep__is_loose, N_MAX, DEF_VAL_INT);
		SET_ZERO(lep__is_medium, N_MAX, DEF_VAL_INT);
		SET_ZERO(lep__is_tight, N_MAX, DEF_VAL_INT);
		SET_ZERO(lep__mass, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__mva, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__p_iso, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__ph_iso, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__phi, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__pt, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__puch_iso, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(lep__rel_iso, N_MAX, DEF_VAL_FLOAT);
		lhe__ht = DEF_VAL_FLOAT;
		lhe__n_b = DEF_VAL_INT;
		lhe__n_c = DEF_VAL_INT;
		lhe__n_e = DEF_VAL_INT;
		lhe__n_g = DEF_VAL_INT;
		lhe__n_j = DEF_VAL_FLOAT;
		lhe__n_l = DEF_VAL_INT;
		met__phi = DEF_VAL_FLOAT;
		met__pt = DEF_VAL_FLOAT;
		met__pt__en_down = DEF_VAL_FLOAT;
		met__pt__en_up = DEF_VAL_FLOAT;
		n__jet = DEF_VAL_INT;
		n__jet_toptagger = DEF_VAL_INT;
		n__jet_toptagger_sj = DEF_VAL_INT;
		n__lep = DEF_VAL_INT;
		n__pv = DEF_VAL_INT;
		n__pvi = DEF_VAL_INT;
		SET_ZERO(pvi__bx, N_MAX, DEF_VAL_INT);
		SET_ZERO(pvi__n0, N_MAX, DEF_VAL_FLOAT);
		SET_ZERO(pvi__ntrue, N_MAX, DEF_VAL_FLOAT);
		weight__pu = DEF_VAL_FLOAT;
		weight__pu__up = DEF_VAL_FLOAT;
		weight__pu_down = DEF_VAL_FLOAT;
		weight__trigger = DEF_VAL_FLOAT;
		weight__trigger_down = DEF_VAL_FLOAT;
		weight__trigger_up = DEF_VAL_FLOAT;
	}
	void make_branches(void) {
		tree->Branch("event__id", &event__id, "event__id/I");
		branch_map["event__id"] = (void*)&event__id;
		tree->Branch("event__json", &event__json, "event__json/I");
		branch_map["event__json"] = (void*)&event__json;
		tree->Branch("event__lumi", &event__lumi, "event__lumi/I");
		branch_map["event__lumi"] = (void*)&event__lumi;
		tree->Branch("event__run", &event__run, "event__run/I");
		branch_map["event__run"] = (void*)&event__run;
		tree->Branch("lhe__n_b", &lhe__n_b, "lhe__n_b/I");
		branch_map["lhe__n_b"] = (void*)&lhe__n_b;
		tree->Branch("lhe__n_c", &lhe__n_c, "lhe__n_c/I");
		branch_map["lhe__n_c"] = (void*)&lhe__n_c;
		tree->Branch("lhe__n_e", &lhe__n_e, "lhe__n_e/I");
		branch_map["lhe__n_e"] = (void*)&lhe__n_e;
		tree->Branch("lhe__n_g", &lhe__n_g, "lhe__n_g/I");
		branch_map["lhe__n_g"] = (void*)&lhe__n_g;
		tree->Branch("lhe__n_l", &lhe__n_l, "lhe__n_l/I");
		branch_map["lhe__n_l"] = (void*)&lhe__n_l;
		tree->Branch("n__jet", &n__jet, "n__jet/I");
		branch_map["n__jet"] = (void*)&n__jet;
		tree->Branch("n__jet_toptagger", &n__jet_toptagger, "n__jet_toptagger/I");
		branch_map["n__jet_toptagger"] = (void*)&n__jet_toptagger;
		tree->Branch("n__jet_toptagger_sj", &n__jet_toptagger_sj, "n__jet_toptagger_sj/I");
		branch_map["n__jet_toptagger_sj"] = (void*)&n__jet_toptagger_sj;
		tree->Branch("n__lep", &n__lep, "n__lep/I");
		branch_map["n__lep"] = (void*)&n__lep;
		tree->Branch("n__pv", &n__pv, "n__pv/I");
		branch_map["n__pv"] = (void*)&n__pv;
		tree->Branch("n__pvi", &n__pvi, "n__pvi/I");
		branch_map["n__pvi"] = (void*)&n__pvi;
		tree->Branch("debug__time1c", &debug__time1c, "debug__time1c/D");
		branch_map["debug__time1c"] = (void*)&debug__time1c;
		tree->Branch("debug__time1r", &debug__time1r, "debug__time1r/D");
		branch_map["debug__time1r"] = (void*)&debug__time1r;
		tree->Branch("gen_jet__eta", gen_jet__eta, "gen_jet__eta[n__jet]/F");
		branch_map["gen_jet__eta"] = (void*)gen_jet__eta;
		tree->Branch("gen_jet__id", gen_jet__id, "gen_jet__id[n__jet]/I");
		branch_map["gen_jet__id"] = (void*)gen_jet__id;
		tree->Branch("gen_jet__mass", gen_jet__mass, "gen_jet__mass[n__jet]/F");
		branch_map["gen_jet__mass"] = (void*)gen_jet__mass;
		tree->Branch("gen_jet__phi", gen_jet__phi, "gen_jet__phi[n__jet]/F");
		branch_map["gen_jet__phi"] = (void*)gen_jet__phi;
		tree->Branch("gen_jet__pt", gen_jet__pt, "gen_jet__pt[n__jet]/F");
		branch_map["gen_jet__pt"] = (void*)gen_jet__pt;
		tree->Branch("gen_jet__status", gen_jet__status, "gen_jet__status[n__jet]/I");
		branch_map["gen_jet__status"] = (void*)gen_jet__status;
		tree->Branch("gen_jet_parton__eta", gen_jet_parton__eta, "gen_jet_parton__eta[n__jet]/F");
		branch_map["gen_jet_parton__eta"] = (void*)gen_jet_parton__eta;
		tree->Branch("gen_jet_parton__id", gen_jet_parton__id, "gen_jet_parton__id[n__jet]/I");
		branch_map["gen_jet_parton__id"] = (void*)gen_jet_parton__id;
		tree->Branch("gen_jet_parton__mass", gen_jet_parton__mass, "gen_jet_parton__mass[n__jet]/F");
		branch_map["gen_jet_parton__mass"] = (void*)gen_jet_parton__mass;
		tree->Branch("gen_jet_parton__phi", gen_jet_parton__phi, "gen_jet_parton__phi[n__jet]/F");
		branch_map["gen_jet_parton__phi"] = (void*)gen_jet_parton__phi;
		tree->Branch("gen_jet_parton__pt", gen_jet_parton__pt, "gen_jet_parton__pt[n__jet]/F");
		branch_map["gen_jet_parton__pt"] = (void*)gen_jet_parton__pt;
		tree->Branch("gen_jet_parton__status", gen_jet_parton__status, "gen_jet_parton__status[n__jet]/I");
		branch_map["gen_jet_parton__status"] = (void*)gen_jet_parton__status;
		tree->Branch("gen_lep__eta", gen_lep__eta, "gen_lep__eta[n__lep]/F");
		branch_map["gen_lep__eta"] = (void*)gen_lep__eta;
		tree->Branch("gen_lep__id", gen_lep__id, "gen_lep__id[n__lep]/I");
		branch_map["gen_lep__id"] = (void*)gen_lep__id;
		tree->Branch("gen_lep__mass", gen_lep__mass, "gen_lep__mass[n__lep]/F");
		branch_map["gen_lep__mass"] = (void*)gen_lep__mass;
		tree->Branch("gen_lep__phi", gen_lep__phi, "gen_lep__phi[n__lep]/F");
		branch_map["gen_lep__phi"] = (void*)gen_lep__phi;
		tree->Branch("gen_lep__pt", gen_lep__pt, "gen_lep__pt[n__lep]/F");
		branch_map["gen_lep__pt"] = (void*)gen_lep__pt;
		tree->Branch("gen_lep__status", gen_lep__status, "gen_lep__status[n__lep]/I");
		branch_map["gen_lep__status"] = (void*)gen_lep__status;
		tree->Branch("gen_met__phi", &gen_met__phi, "gen_met__phi/F");
		branch_map["gen_met__phi"] = (void*)&gen_met__phi;
		tree->Branch("gen_met__pt", &gen_met__pt, "gen_met__pt/F");
		branch_map["gen_met__pt"] = (void*)&gen_met__pt;
		tree->Branch("jet__bd_csv", jet__bd_csv, "jet__bd_csv[n__jet]/F");
		branch_map["jet__bd_csv"] = (void*)jet__bd_csv;
		tree->Branch("jet__ce_e", jet__ce_e, "jet__ce_e[n__jet]/F");
		branch_map["jet__ce_e"] = (void*)jet__ce_e;
		tree->Branch("jet__ch_e", jet__ch_e, "jet__ch_e[n__jet]/F");
		branch_map["jet__ch_e"] = (void*)jet__ch_e;
		tree->Branch("jet__el_e", jet__el_e, "jet__el_e[n__jet]/F");
		branch_map["jet__el_e"] = (void*)jet__el_e;
		tree->Branch("jet__energy", jet__energy, "jet__energy[n__jet]/F");
		branch_map["jet__energy"] = (void*)jet__energy;
		tree->Branch("jet__eta", jet__eta, "jet__eta[n__jet]/F");
		branch_map["jet__eta"] = (void*)jet__eta;
		tree->Branch("jet__id", jet__id, "jet__id[n__jet]/I");
		branch_map["jet__id"] = (void*)jet__id;
		tree->Branch("jet__pileupJetId", jet__pileupJetId, "jet__pileupJetId[n__jet]/F");
		branch_map["jet__pileupJetId"] = (void*)jet__pileupJetId;
		tree->Branch("jet__mass", jet__mass, "jet__mass[n__jet]/F");
		branch_map["jet__mass"] = (void*)jet__mass;
		tree->Branch("jet__mu_e", jet__mu_e, "jet__mu_e[n__jet]/F");
		branch_map["jet__mu_e"] = (void*)jet__mu_e;
		tree->Branch("jet__ne_e", jet__ne_e, "jet__ne_e[n__jet]/F");
		branch_map["jet__ne_e"] = (void*)jet__ne_e;
		tree->Branch("jet__nh_e", jet__nh_e, "jet__nh_e[n__jet]/F");
		branch_map["jet__nh_e"] = (void*)jet__nh_e;
		tree->Branch("jet__ph_e", jet__ph_e, "jet__ph_e[n__jet]/F");
		branch_map["jet__ph_e"] = (void*)jet__ph_e;
		tree->Branch("jet__phi", jet__phi, "jet__phi[n__jet]/F");
		branch_map["jet__phi"] = (void*)jet__phi;
		tree->Branch("jet__pt", jet__pt, "jet__pt[n__jet]/F");
		branch_map["jet__pt"] = (void*)jet__pt;
		tree->Branch("jet__vtxMass", jet__vtxMass, "jet__vtxMass[n__jet]/F");
		branch_map["jet__vtxMass"] = (void*)jet__vtxMass;
		tree->Branch("jet__vtxNtracks", jet__vtxNtracks, "jet__vtxNtracks[n__jet]/I");
		branch_map["jet__vtxNtracks"] = (void*)jet__vtxNtracks;
		tree->Branch("jet__vtx3DVal", jet__vtx3DVal, "jet__vtx3DVal[n__jet]/F");
		branch_map["jet__vtx3DVal"] = (void*)jet__vtx3DVal;
		tree->Branch("jet__vtx3DSig", jet__vtx3DSig, "jet__vtx3DSig[n__jet]/F");
		branch_map["jet__vtx3DSig"] = (void*)jet__vtx3DSig;
		tree->Branch("jet_toptagger__energy", jet_toptagger__energy, "jet_toptagger__energy[n__jet_toptagger]/F");
		branch_map["jet_toptagger__energy"] = (void*)jet_toptagger__energy;
		tree->Branch("jet_toptagger__eta", jet_toptagger__eta, "jet_toptagger__eta[n__jet_toptagger]/F");
		branch_map["jet_toptagger__eta"] = (void*)jet_toptagger__eta;
		tree->Branch("jet_toptagger__mass", jet_toptagger__mass, "jet_toptagger__mass[n__jet_toptagger]/F");
		branch_map["jet_toptagger__mass"] = (void*)jet_toptagger__mass;
		tree->Branch("jet_toptagger__min_mass", jet_toptagger__min_mass, "jet_toptagger__min_mass[n__jet_toptagger]/F");
		branch_map["jet_toptagger__min_mass"] = (void*)jet_toptagger__min_mass;
		tree->Branch("jet_toptagger__n_sj", jet_toptagger__n_sj, "jet_toptagger__n_sj[n__jet_toptagger]/I");
		branch_map["jet_toptagger__n_sj"] = (void*)jet_toptagger__n_sj;
		tree->Branch("jet_toptagger__phi", jet_toptagger__phi, "jet_toptagger__phi[n__jet_toptagger]/F");
		branch_map["jet_toptagger__phi"] = (void*)jet_toptagger__phi;
		tree->Branch("jet_toptagger__pt", jet_toptagger__pt, "jet_toptagger__pt[n__jet_toptagger]/F");
		branch_map["jet_toptagger__pt"] = (void*)jet_toptagger__pt;
		tree->Branch("jet_toptagger__top_mass", jet_toptagger__top_mass, "jet_toptagger__top_mass[n__jet_toptagger]/F");
		branch_map["jet_toptagger__top_mass"] = (void*)jet_toptagger__top_mass;
		tree->Branch("jet_toptagger__w_mass", jet_toptagger__w_mass, "jet_toptagger__w_mass[n__jet_toptagger]/F");
		branch_map["jet_toptagger__w_mass"] = (void*)jet_toptagger__w_mass;
		tree->Branch("jet_toptagger_sj__energy", jet_toptagger_sj__energy, "jet_toptagger_sj__energy[n__jet_toptagger_sj]/F");
		branch_map["jet_toptagger_sj__energy"] = (void*)jet_toptagger_sj__energy;
		tree->Branch("jet_toptagger_sj__eta", jet_toptagger_sj__eta, "jet_toptagger_sj__eta[n__jet_toptagger_sj]/F");
		branch_map["jet_toptagger_sj__eta"] = (void*)jet_toptagger_sj__eta;
		tree->Branch("jet_toptagger_sj__mass", jet_toptagger_sj__mass, "jet_toptagger_sj__mass[n__jet_toptagger_sj]/F");
		branch_map["jet_toptagger_sj__mass"] = (void*)jet_toptagger_sj__mass;
		tree->Branch("jet_toptagger_sj__phi", jet_toptagger_sj__phi, "jet_toptagger_sj__phi[n__jet_toptagger_sj]/F");
		branch_map["jet_toptagger_sj__phi"] = (void*)jet_toptagger_sj__phi;
		tree->Branch("jet_toptagger_sj__pt", jet_toptagger_sj__pt, "jet_toptagger_sj__pt[n__jet_toptagger_sj]/F");
		branch_map["jet_toptagger_sj__pt"] = (void*)jet_toptagger_sj__pt;
		tree->Branch("lep__ch_iso", lep__ch_iso, "lep__ch_iso[n__lep]/F");
		branch_map["lep__ch_iso"] = (void*)lep__ch_iso;
		tree->Branch("lep__charge", lep__charge, "lep__charge[n__lep]/I");
		branch_map["lep__charge"] = (void*)lep__charge;
		tree->Branch("lep__dxy", lep__dxy, "lep__dxy[n__lep]/F");
		branch_map["lep__dxy"] = (void*)lep__dxy;
		tree->Branch("lep__dz", lep__dz, "lep__dz[n__lep]/F");
		branch_map["lep__dz"] = (void*)lep__dz;
		tree->Branch("lep__ec_iso", lep__ec_iso, "lep__ec_iso[n__lep]/F");
		branch_map["lep__ec_iso"] = (void*)lep__ec_iso;
		tree->Branch("lep__eta", lep__eta, "lep__eta[n__lep]/F");
		branch_map["lep__eta"] = (void*)lep__eta;
		tree->Branch("lep__hc_iso", lep__hc_iso, "lep__hc_iso[n__lep]/F");
		branch_map["lep__hc_iso"] = (void*)lep__hc_iso;
		tree->Branch("lep__id", lep__id, "lep__id[n__lep]/I");
		branch_map["lep__id"] = (void*)lep__id;
		tree->Branch("lep__id_bitmask", lep__id_bitmask, "lep__id_bitmask[n__lep]/I");
		branch_map["lep__id_bitmask"] = (void*)lep__id_bitmask;
		tree->Branch("lep__is_loose", lep__is_loose, "lep__is_loose[n__lep]/I");
		branch_map["lep__is_loose"] = (void*)lep__is_loose;
		tree->Branch("lep__is_medium", lep__is_medium, "lep__is_medium[n__lep]/I");
		branch_map["lep__is_medium"] = (void*)lep__is_medium;
		tree->Branch("lep__is_tight", lep__is_tight, "lep__is_tight[n__lep]/I");
		branch_map["lep__is_tight"] = (void*)lep__is_tight;
		tree->Branch("lep__mass", lep__mass, "lep__mass[n__lep]/F");
		branch_map["lep__mass"] = (void*)lep__mass;
		tree->Branch("lep__mva", lep__mva, "lep__mva[n__lep]/F");
		branch_map["lep__mva"] = (void*)lep__mva;
		tree->Branch("lep__p_iso", lep__p_iso, "lep__p_iso[n__lep]/F");
		branch_map["lep__p_iso"] = (void*)lep__p_iso;
		tree->Branch("lep__ph_iso", lep__ph_iso, "lep__ph_iso[n__lep]/F");
		branch_map["lep__ph_iso"] = (void*)lep__ph_iso;
		tree->Branch("lep__phi", lep__phi, "lep__phi[n__lep]/F");
		branch_map["lep__phi"] = (void*)lep__phi;
		tree->Branch("lep__pt", lep__pt, "lep__pt[n__lep]/F");
		branch_map["lep__pt"] = (void*)lep__pt;
		tree->Branch("lep__puch_iso", lep__puch_iso, "lep__puch_iso[n__lep]/F");
		branch_map["lep__puch_iso"] = (void*)lep__puch_iso;
		tree->Branch("lep__rel_iso", lep__rel_iso, "lep__rel_iso[n__lep]/F");
		branch_map["lep__rel_iso"] = (void*)lep__rel_iso;
		tree->Branch("lhe__ht", &lhe__ht, "lhe__ht/F");
		branch_map["lhe__ht"] = (void*)&lhe__ht;
		tree->Branch("lhe__n_j", &lhe__n_j, "lhe__n_j/F");
		branch_map["lhe__n_j"] = (void*)&lhe__n_j;
		tree->Branch("met__phi", &met__phi, "met__phi/F");
		branch_map["met__phi"] = (void*)&met__phi;
		tree->Branch("met__pt", &met__pt, "met__pt/F");
		branch_map["met__pt"] = (void*)&met__pt;
		tree->Branch("met__pt__en_down", &met__pt__en_down, "met__pt__en_down/F");
		branch_map["met__pt__en_down"] = (void*)&met__pt__en_down;
		tree->Branch("met__pt__en_up", &met__pt__en_up, "met__pt__en_up/F");
		branch_map["met__pt__en_up"] = (void*)&met__pt__en_up;
		tree->Branch("pvi__bx", pvi__bx, "pvi__bx[n__pvi]/I");
		branch_map["pvi__bx"] = (void*)pvi__bx;
		tree->Branch("pvi__n0", pvi__n0, "pvi__n0[n__pvi]/F");
		branch_map["pvi__n0"] = (void*)pvi__n0;
		tree->Branch("pvi__ntrue", pvi__ntrue, "pvi__ntrue[n__pvi]/F");
		branch_map["pvi__ntrue"] = (void*)pvi__ntrue;
		tree->Branch("weight__pu", &weight__pu, "weight__pu/F");
		branch_map["weight__pu"] = (void*)&weight__pu;
		tree->Branch("weight__pu__up", &weight__pu__up, "weight__pu__up/F");
		branch_map["weight__pu__up"] = (void*)&weight__pu__up;
		tree->Branch("weight__pu_down", &weight__pu_down, "weight__pu_down/F");
		branch_map["weight__pu_down"] = (void*)&weight__pu_down;
		tree->Branch("weight__trigger", &weight__trigger, "weight__trigger/F");
		branch_map["weight__trigger"] = (void*)&weight__trigger;
		tree->Branch("weight__trigger_down", &weight__trigger_down, "weight__trigger_down/F");
		branch_map["weight__trigger_down"] = (void*)&weight__trigger_down;
		tree->Branch("weight__trigger_up", &weight__trigger_up, "weight__trigger_up/F");
		branch_map["weight__trigger_up"] = (void*)&weight__trigger_up;
	}
};
