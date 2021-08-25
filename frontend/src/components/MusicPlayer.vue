<template>
   <b-container fluid = sm>
      <b-row class="justify-content-md-center" cols = "2">
            <b-card title = "song.title" style= " max-width: 35em;" class = "mb-1" >
               <b-card-text>
                  <div lass="text-center" id = "wf">
                   </div> 
                   <br>
                    <div class="text-center">
                        <b-button-group class="mx-1">
                           <b-button pill v-on:click="playPause"  variant="primary">Play/Pause</b-button>
                         </b-button-group>      
                     </div>
                 
               </b-card-text>
            </b-card>
          </b-row>
         <b-row class="justify-content-md-center" cols = "2">
               <b-card title = "New Comment" style="max-width: 35rem;" class = "mb-1">
                  <b-form @submit="postComments">
                     <b-form-group label = "username"  >  </b-form-group >
                     <b-form-input v-model = "userC.username" @change= "updateTimeStamp" required ></b-form-input>
                     <b-form-group label = "Timestamp" >  </b-form-group >
                     <b-form-input v-model = "userC.timeStamp" required ></b-form-input>
                     <b-form-group label = "comment" >  </b-form-group >
                     <b-form-textarea v-model = "userC.comment" required ></b-form-textarea>
                     <div class="text-center">
                        <b-button-group class="mx-1">
                           <b-button pill type = "submit" variant="primary">Submit</b-button>
                        </b-button-group>
                     </div>
                  </b-form>
               </b-card>
         </b-row >
          <b-row class="justify-content-md-center" cols = "2">
            <b-card title = "User Comments" style="max-width: 35rem;" class = "mb-1">
            <b-list-group>
               <div v-for = "uc in userComB" :key = "uc.id">
                  <b-list-group-item class="d-flex align-items-center">
                   <b-avatar variant="info" src="uc.image" class="mr-3"></b-avatar>
                       <span class="mr-auto">{{uc.username}} at  {{uc.timeStamp + ': ' + uc.comment }}   </span>
                  </b-list-group-item>
                  <br>
               </div>
            </B-list-group>
          </b-card>
         </b-row >
   </b-container>
</template>

<script>
import axios from 'axios'
import WaveSurfer from "wavesurfer.js";

export default {
    data () {
      return {
         waveSurfer : {},
         userC :  {
               username : "", 
               comment : "", 
               timeStamp: "", 
         },// userC
         userComB: null, 
         file: require('../assets/A.mp3'), 
         options: {
               backend :"WebAudio",
               barHeight : 2,
               mediaControls : true, 
         },
         chageState: true,
       
      }
   }, 
   async created() {
         await(this.getComments())
            this.waveFrom()
          },

   methods: {
      async postComments () {
         try {
               await(axios.post ('http://localhost:8000/api/post', this.userC))
         }
         catch (error) {
            console.log(error)
         }
      }, 
      async getComments () {
         try {
             this.userComB = (await(axios.get('http://localhost:8000/api/all'))).data;
             console.log(this.userComB)
         }
         catch (error) {
            console.log(error)
         }
      }, 
      playPause() {
           this.waveSurfer.playPause()
           if (this.waveSurfer.isPlaying()) {
                this.getTime()
           }
      },
      
      updateTimeStamp () {
         if (this.userC.username.length == 0) {
            this.chageState = true
         }
        else if (this.chageState == true) {
             this.getTime()
             this.chageState = false
         }
      }, 
      waveFrom() {
         let options = this.options;
         let wsOptions = Object.assign({ container:"#wf" }, options);
         this.waveSurfer = new WaveSurfer.create(wsOptions);
         this.waveSurfer.load(this.file);
      }, 
      getTime (){
               var sec = this.waveSurfer.getCurrentTime();
               sec =  sec/60 
               sec = sec.toFixed(2)
               var string = sec.toString(); 
               string = string.replace('.', ':')
               this.userC.timeStamp = string
      }
   }
}

</script>


