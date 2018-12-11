import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-unmunching',
  templateUrl: './unmunching.component.html',
  styleUrls: ['./unmunching.component.scss']
})
export class UnmunchingComponent implements OnInit {
  unmunchedData$: Object
  check$: Object
  show$: Object
  showList: Boolean
  fileToUpload: File = null;
  wordsList: Object  

  constructor(
  	private data: DataService,
  	private route: ActivatedRoute,
  	private location: Location) { }

  ngOnInit() {
    this.check$ = [];
    this.show$ = [];
    this.showList = false;
    this.wordsList =[];
  }

  goBack(): void {
    this.location.back();
  }

  showForms(id) {
    this.show$[id] = !this.show$[id];
  }

  /**
   * this function send the WordList to the backend
   * and receive the processed data
   */
  uploadWordList(files: FileList) {
    this.fileToUpload = files.item(0);
    const fileReader = new FileReader();
    var _this = this;
    fileReader.onload = function(e) {
      var text = fileReader.result;
      var wordsArray = text.split("\n");
      console.log(wordsArray);
      _this.data.getUnmunch(wordsArray).subscribe(
        data =>
        {
          _this.unmunchedData$ = data["candidate_words"];
          console.log(_this.unmunchedData$);
          _this.showList = true;
        }
        );
    }
    fileReader.readAsText(this.fileToUpload, "UTF-8");
  }

  /**
  this function is to add the selected words to the paradigm
  **/
  addWords(){

  }
  
}
