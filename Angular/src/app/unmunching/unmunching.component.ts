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
  

  constructor(
  	private data: DataService,
  	private route: ActivatedRoute,
  	private location: Location) { }

  ngOnInit() {
    this.check$ = [];
    this.show$ = [];
    this.showList = false;
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
  uploadWordList() {
    this.unmunchedData$ = this.data.getUnmunch();
    this.showList = true;
  }

  /**
   * this function send the selected data to the backend 
   */
  addWords() {
    
  }

  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
  }

  uploadFileToActivity() {
    // this.data.postFile(this.fileToUpload).subscribe(data => {
    //   // do something, if upload success
    //   alert("File upload successful");
    //   }, error => {
    //     console.log(error);
    //   });
    const fileReader = new FileReader();
    fileReader.onload = function(e) {
    var text = fileReader.result;
    }
    fileReader.readAsText(this.fileToUpload, "UTF-8");
    console.log(this.fileToUpload);
  }

}
