// app.js


var speech = new webkitSpeechRecognition();
// app.js


var btn = document.getElementById('btn');
var content = document.getElementById('content');



//言語を日本語に設定
speech.lang = "ja";

speech.interimResults = true;
speech.continuous = true;

btn.addEventListener( 'click' , function() {


    // ➀ボタンをクリックした時の処理
    speech.start();

} );



// app.js


speech.addEventListener( 'result' , function( e ) {
    // 音声認識で取得した情報を、コンソール画面に表示
    var text = e.results[0][0].transcript;
    document.getElementById("dog").play();


    // 「ビデオ」と認識されたら指定の関数を実行
    if( text === "今年は" ) recognitionA.start();

    if( text === "季節は" ) recognitionB.start();

    if( text === "明日は" ) recognitionC.start();

    if( text === "都道府県は" ) recognitionD.start();

    if( text === "地方" ) recognitionE.start();


} );

var recognitionA = new webkitSpeechRecognition();
  recognitionA.onresult = function(event) {
  if (event.results.length > 0) {
    a.value = event.results[0][0].transcript;
  }
}
var recognitionB = new webkitSpeechRecognition();
  recognitionB.onresult = function(event) {
  if (event.results.length > 0) {
    b.value = event.results[0][0].transcript;
  }
}

var recognitionC = new webkitSpeechRecognition();
  recognitionC.onresult = function(event) {
  if (event.results.length > 0) {
    c.value = event.results[0][0].transcript;
  }
}

var recognitionD = new webkitSpeechRecognition();
  recognitionD.onresult = function(event) {
  if (event.results.length > 0) {
    c.value = event.results[0][0].transcript;
  }
}

var recognitionE = new webkitSpeechRecognition();
  recognitionE.onresult = function(event) {
  if (event.results.length > 0) {
    c.value = event.results[0][0].transcript;
  }
}