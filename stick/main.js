//documentからid属性がresultである要素を取得する
const timeInput = document.getElementById('timeInput');

//documentから「最大値」ボタン取得
const goStick = document.querySelector('#goStick button');

var data;


function Stick(timeInput){
	this.data = timeInput.value;

	this.time1 = this.data.split('\n');

	this.timeDate = function(){
		return this.time1;
	}
}



goStick.addEventListener('click',()=>{
	// クリック時にデータを取得
	data = timeInput.value;
	var Stick1 = new Stick(timeInput);
	console.log(Stick1.data);
	console.log(data);
	console.log(timeInput.value);
});