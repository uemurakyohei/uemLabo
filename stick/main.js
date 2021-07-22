//documentからid属性がresultである要素を取得する
const timeInput = document.getElementById('timeInput');

//documentから「最大値」ボタン取得
const goStick = document.querySelector('#goStick button');

var data;


function Stick(timeInput){
	this.data = timeInput.value;
	//inputに入れた値をバラバラにする
	this.time = this.data.split(/[\n\-\:]/);

	this.timeData = [];

	this.timeDate = function(){
		this.time = this.time.filter(Boolean);
		//this.time = this.time.split('\-');
		let array = [];
		for (let i = 1; i < this.time.length+1; i ++) {
			
			array.push(this.time[i-1]);
			console.log(array);
			if (i%4 == 0){
				this.timeData.push(array);
				array = [];
			}
		}
	}

	//時間数を分単位に変換 10:20→t2T(10,20)→80
	this.t2T = function(t1,t2){
		let TIME = t1*60 + t2;
		return TIME
	}



	//拘束時間、実働時間の計算
	this.calcTime = function(){
		TIME = C-A;
		SHIFT = D-B;
		
		if (SHIFT < TIME){
			if SHIFT < 480
				SHOTEINAI = 480 - SHIFT;
				SHOTEIGAI = TIME - 480;
			else
				SHOTEIGAI = SHIFT - TIME;
		}
	}







}



goStick.addEventListener('click',()=>{
	// クリック時にデータを取得
	data = timeInput.value;
	var Stick1 = new Stick(timeInput);
	console.log(Stick1.timeDate());
});


/*
10:00-20:00
10:00-17:00

10:00-15:00
10:00-20:00
*/