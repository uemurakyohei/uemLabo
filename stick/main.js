//documentからid属性がresultである要素を取得する
const timeInput = document.getElementById('timeInput');

//documentから「最大値」ボタン取得
const goStick = document.querySelector('#goStick button');

//inputの要素を格納
var data;

//documentからid属性がstickBoxである要素を取得する
const stickBox = document.getElementById('resuletBox');

function Stick(timeInput){
	this.data = timeInput.value;
	//inputに入れた数値をバラバラにする
	this.time = this.data.split(/[\n\-\:]/);
	this.time = this.time.filter(Boolean);
	this.timeData = [];

	//所定内、法定内、法定外
	this.SHOTEIGAI = 0;
	this.SHOTEINAI  = 0;
	this.PLANTIME = 0;



		
	//所定内、法定内、法定外をDOMに代入する、stick!作成
	this.addValue = function(){
		this.defineTime();
		let stick = document.createElement("div");
		stick.className = "stick";

		let planedStick = document.createElement("div");
		planedStick.className = "planedStick";

		let workStick = document.createElement("div");
		workStick.className = "workStick";
		

		let overTime = this.divMake('overTime',this.SHOTEIGAI);
		workStick.appendChild(overTime);
		
		let outTime = this.divMake('outTime',this.SHOTEINAI);
		workStick.appendChild(outTime);

		let planTime = this.divMake('planTime',this.PLANTIME);
		workStick.appendChild(planTime);



		stick.appendChild(workStick);
		stickBox.appendChild(stick);
	}


	//値を定義する
	this.defineTime = function(){
		// array:時間帯を格納
		let array = [];
		// array2:時間数を格納
		let array2 = [];

		//分単位で時間を格納
		for (let i = 1; i < this.time.length+1; i+=2) {
			let TIME = this.t2T(Number(this.time[i-1]),Number(this.time[i]));
			array.push(TIME);
			}
		console.log('array',array);

		//時間数を計算
		for (let j = 1; j < array.length+1; j+=2) {
			let VALUE = this.time2value(array[j-1],array[j]);
			array2.push(VALUE);
			}
		console.log('array2',array2);


		//所定内、法定内、法定外を計算する
		for (let k = 1; k < array2.length+1; k+=2) {
			this.calcTime(array2[k-1],array2[k]);
			}
	}

	//stickの子要素divを作成
	this.divMake = function(divName,Time){
		let Name = divName;
		//分で計算した値を時間数として扱う
		let time = this.T2t(Time);
		let div = document.createElement("div");
		div.className= Name;
		div.textContent = time;
		div.style.height = time*10 + "px";
		return div;
	}





	//時間数を分単位に変換 10:20→t2T(10,20)→80
	this.t2T = function(t1,t2){
		let TIME = t1*60 + t2;
		return TIME
	}

	//分単位を時間数に変換 90→1.5
	this.T2t = function(TIME){
		let time =Math.floor(TIME/60*100)/100;
		return time
	}

	//時間数を算出
	this.time2value = function(t1,t2){
		let value = t2 -t1;
		return value;
	}



	//拘束時間、実働時間の計算
	//TIME:実働時間,SHIFT:シフトの時間
	this.calcTime = function(SHIFT,TIME){		
		if (SHIFT < TIME){
			//シフト時間が8hより下
			if (SHIFT < 480){
				this.SHOTEINAI = 480 - SHIFT;
				this.SHOTEIGAI = TIME - 480;
				this.PLANTIME = SHIFT;
			}
			//シフト時間が8h以上
			else{
				this.SHOTEIGAI = SHIFT - TIME;
				this.PLANTIME = SHIFT;
			}
		}
		else{
			this.PLANTIME = TIME;
		}
		console.log("shift",SHIFT);
		console.log("time",TIME);
		console.log("shotei",this.SHOTEINAI);
		console.log("shoteigai",this.SHOTEIGAI);
		console.log("plantime",this.PLANTIME);
	}


}



goStick.addEventListener('click',()=>{
	// クリック時にデータを取得
	data = timeInput.value;
	let Stick1 = new Stick(timeInput);
	Stick1.addValue();
	//console.log(Stick1.timeDate());
});


/*
10:10-17:20
10:30-20:50

10:00-15:00
10:00-20:00

	//一日のシフトと実働を一つの配列に入れ込む
	this.timeDate = function(){
		//空白要素を削除
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






*/