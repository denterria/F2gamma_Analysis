#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <TError.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TStyle.h>
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include "TSystem.h"
#include "TObject.h"
#include <fstream>
#include <iostream>
#include <vector>



void Plot(){

std::string Input = "~/F2_Analysis/10Prozent/";
std::string Output = "~/F2_Analysis/10Prozent/";






std::vector<std::string> File ={"Q2_9_0","Q2_7_5","Q2_6_8","Q2_2_8","Q2_2_4","Q2_1_9","Q2_0_24","Q2_0_38","Q2_0_71","Q2_1_3","Q2_1_9","Q2_2_4","Q2_2_8","Q2_3_7","Q2_4_3","Q2_5_0","Q2_5_3","Q2_5_9","Q2_6_8","Q2_7_5","Q2_9_0","Q2_9_2","Q2_9_9","Q2_10_8","Q2_11_0","Q2_12_0","Q2_12_5", "Q2_14_5", "Q2_15_3", "Q2_16_0", "Q2_17_3", "Q2_17_5", "Q2_17_8", "Q2_20_0", "Q2_20_7", "Q2_23_0", "Q2_24_0", "Q2_30_0", "Q2_39_7", "Q2_41_0", "Q2_45_0", "Q2_59_0", "Q2_60_0","Q2_67_2","Q2_73_0","Q2_76_4","Q2_80_0",
"Q2_90_0","Q2_100_0","Q2_120_0","Q2_125_0","Q2_135_0","Q2_225_0","Q2_284_0","Q2_390_0",
"Q2_780_0"};




for(int i = 0; i <= File.size(); i++){
	
	
	//Form("Normalised events / %2.1f GeV", h_mlb->GetBinWidth(1))
	std::string Path = Input + File[i] +"/output/" + "plots.root";
	std::cout<<Path<<std::endl;
	std::cout<<"File ok ?"<<std::endl;
	
	
	
	
	
	
	if(Path.c_str()){
	TFile f(Path.c_str());
	TCanvas* c2 = (TCanvas*) f.Get("Canvas/data_4043-1");
	TCanvas* c1 = (TCanvas*) f.Get("Canvas/data_4041-1");
	TCanvas* c3 = (TCanvas*) f.Get("Canvas/data_4051-1");
	TCanvas* c4 = (TCanvas*) f.Get("Canvas/data_4042-1");
	TCanvas* c5 = (TCanvas*) f.Get("Canvas/data_4052-1");
	
	std::string out = Output + File[i] + "plot.png" ;
	
	if(c2){
	c2->Draw();
	c2->SaveAs(out.c_str());
	};

	if(c1){
	c1->Draw();
	c1->SaveAs(out.c_str());
	};
	
	if(c3){
	c3->Draw();
	c3->SaveAs(out.c_str());
	};
	
	
	if(c4){
	c4->Draw();
	c4->SaveAs(out.c_str());
	};
	if(c5){
	c5->Draw();
	c5->SaveAs(out.c_str());
	};
	
std::string Tex = Form("\begin{figure} \centering \includegraphics[width=0.2\linewidth]{%s} \end{figure}", Path.c_str());


	}else continue;






for(int i = 0; i <= File.size(); i++){
	std::string out2 = Output + File[i] + "plot.png" ;
	std::string Tex2 = Form("\includegraphics[width=0.2\linewidth]{%s}", out2.c_str());
	std::cout<<Tex2<<std::endl;
};
};




/*
if(c2){
c2->Draw();
c2->SaveAs("~/Desktop/abcd.png");
};

if(c1){
c1->Draw();
c1->SaveAs("~/Desktop/abcd1.png");
};

*/

}



/*

void loop(const char* ext = ".C")
{
  const char* inDir = "$ROOTSYS/tutorials";

  char* dir = gSystem->ExpandPathName(inDir);
  void* dirp = gSystem->OpenDirectory(dir);

  const char* entry;
  const char* filename[100];
  Int_t n = 0;
  TString str;

  while((entry = (char*)gSystem->GetDirEntry(dirp))) {
    str = entry;
    if(str.EndsWith(ext))
      filename[n++] = gSystem->ConcatFileName(dir, entry);
  }

  for (Int_t i = 0; i < n; i++)
    Printf("file -> %s", filename[i]);
}
*/
