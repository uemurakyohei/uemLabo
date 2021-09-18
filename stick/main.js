//documentからid属性がresultである要素を取得する
const timeInput = document.getElementById('timeInput');

//documentから「最大値」ボタン取得
const goStick = document.querySelector('#goStick button');

//inputの要素を格納
var data;

//documentからid属性がstickBoxである要素を取得する
const stickBox = document.getElementById('resuletBox');

//作成した棒グラフの数を数える
let classCount = 0;

/////////////////
//時間の加工//////timeInput(~)→array[p1,w1,p2,w2...]
/////////////////
class inputTimeEditer{
	constructor(timeInput){
		this.data = timeInput.value;
		//inputに入れた数値をバラバラにする
		this.time = this.data.split(/[\n\-\:]/);
		this.time = this.time.filter(Boolean);
		//時間帯のそれぞれの開始時間と終了時間を分単位で収納
		this.inputTime = [];
		//一日の時間数をそれぞれ分単位で収納
		this.inputTimeMin = [];

	}
	
	//実行する用のコンストラクタをセット
	make = function(){
		this.int2num();
		this.defineTime();
	}

	//input要素の中の文字列を数値に変換
	int2num = function(){
		const array = this.time;
		//時間数を計算
		for (let i = 0; i < this.time.length; i++) {
			//公休日(x)の時に0をセットする
			if(array[i]=="x"){
				let j = 0;
				do {
				j ++;
				this.inputTime.push(0);
				} while (j < 4);
			}
			else if(Number(array[i])|Number(array[i])==0){
				this.inputTime.push(Number(array[i]));
			}
			else{
				//inputに時間以外の入力があった時にエラー処理を行う予定
				//★★フラグを立てる処理が必要？
				console.log("error number",i,"is",(array[i]));
			}
		}
	}


	//値を定義する
	defineTime = function(){
		// array:時間帯を格納
		let array = [];
		// array2:時間数を格納
		let array2 = [];

		//分単位で時間を格納
		for (let i = 0; i < this.inputTime.length; i+=2) {
			let TIME = this.t2T(this.inputTime[i],this.inputTime[i+1]);
			array.push(TIME);
		}
		console.log('array',array);

		//時間数を計算
		for (let j = 0; j < array.length; j+=2) {
			let VALUE = this.time2value(array[j],array[j+1]);
			array2.push(VALUE);
		}
		console.log('array2',array2);
		this.inputTimeMin = array2;
		console.log('this.inputTimeMin',this.inputTimeMin);
	}

	//時間数を分単位に変換 10:20→t2T(10,20)→80
	t2T = function(t1,t2){
		let TIME = t1*60 + t2;
		return TIME
	}

	//時間数を算出
	time2value = function(t1,t2){
		let value = t2 - t1;
		return value;
	}

}

/////////////////
//1日ごとの計算///day(planTime,workTime)→day.SHOTEIGAI,SHOTEINAI,PLANTIME
/////////////////
class day{
	constructor(planTime,workTime){

		this.planTime = planTime;
		this.workTime = workTime;

		//所定内、法定内、法定外
		this.SHOTEIGAI = 0;
		this.SHOTEINAI  = 0;
		this.PLANTIME = 0

		classCount +=1;
	}
		
	// //所定内、法定内、法定外をDOMに代入する、stick!作成
	// addValue = function(){
	// 	this.defineTime();

	// 	let stick = this.divMake('stick',99);
	// 	let planedStick = this.divMake('planedStick',99);
	// 	let workStick = this.divMake('workStick',99);
		
	// 	let overTime = this.divMake('overTime',this.SHOTEIGAI);
	// 	workStick.appendChild(overTime);
		
	// 	let outTime = this.divMake('outTime',this.SHOTEINAI);
	// 	workStick.appendChild(outTime);

	// 	let planTime = this.divMake('planTime',this.PLANTIME);
	// 	workStick.appendChild(planTime);



	// 	stick.appendChild(workStick);
	// 	stickBox.appendChild(stick);
	// }


	//値を定義する
	defineTime = function(){
		this.calcTime(this.planTime,this.workTime);
	}

	//divを作成
	divMake = function(divName,Time){


		let div = document.createElement("div");
		div.className= divName;

		if(Time==0){
			//0の時にはdivを作成しない
			div.style.height = 0 + "px";
		}
		else if(Time!=99){
			//99:class=stickの時には不要な要素
			//分で計算した値を時間数として扱う
			let time = this.T2t(Time);
			div.textContent = time;
			div.style.height = time*10 + "px";
		}
		return div;
	}
	



	//分単位を時間数に変換 90→1.5
	T2t = function(TIME){
		let time =Math.floor(TIME/60*100)/100;
		return time
	}




	//拘束時間、実働時間の計算
	//TIME:実働時間,SHIFT:シフトの時間
	calcTime = function(SHIFT,TIME){		
		if (SHIFT == null){
			SHIFT = 0;
		}
		if(TIME == null){
			TIME = 0;
		}
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

	//静的メソッドで呼び出し可能:Stick.static()
	static count(){
		return classCount;
	}



	//データのリセット★★要検討
	resetValue = function(){
		this.time = 0;
		this.timeData = [];

		//所定内、法定内、法定外
		this.SHOTEIGAI = 0;
		this.SHOTEINAI  = 0;
		this.PLANTIME = 0

		//すでにstickが作成されていたら消去する
		let oldStick = document.getElementsByClassName('stick');
		if(oldStick){
			oldStick.innerHTML = '';
			oldStick.remove;
		}
	}


}


/////////////////
//1週ごとの計算///
/////////////////
class week{
	constructor(timeInput){
		this.data = timeInput.value;
		//inputに入れた数値をバラバラにする
		this.time = this.data.split(/[\n\-\:]/);
		this.time = this.time.filter(Boolean);
		this.timeData = [];

		//所定内、法定内、法定外
		this.SHOTEIGAI = 0;
		this.SHOTEINAI  = 0;
		this.PLANTIME = 0

		classCount +=1;
	}
		
	//所定内、法定内、法定外をDOMに代入する、stick!作成
	addValue = function(){
		this.defineTime();
	}
}




/////////////////
//stick module///→day、classを呼び出し描画する
/////////////////
class stickModule{
	constructor(timeInput){
		this.data = timeInput;
	}
	
	//inputTimeEditer classを使ってデータの読み込み
	makeStick = function(){
		this.inputTime();
	}

	

	
	inputTime = function(){
		//inputTimeEditerを使ってデータの読み込み
		let inputTimeEditer1 = new inputTimeEditer(this.data);
		inputTimeEditer1.make();
		const array = inputTimeEditer1.inputTimeMin;

		this.addValue(array);

	}

	//所定内、法定内、法定外をDOMに代入する、stick!作成
	addValue = function(array){

		let stick = this.divMake('stick',99);
		let planedStick = this.divMake('planedStick',99);


		console.log("長さ",array.length);

		//day classを使って日毎にインスタンスを作成
		//1日ごとの勤怠時間を計算
		for (let i = 0; i < array.length; i+=2) {

			let workStick = this.divMake('workStick',99);


			let days = new day(array[i],array[i+1]);	
			days.defineTime();

			console.log("1所定外",days.SHOTEIGAI);
			
			let overTime = this.divMake('overTime',days.SHOTEIGAI);
			workStick.appendChild(overTime);
			
			let outTime = this.divMake('outTime',days.SHOTEINAI);
			workStick.appendChild(outTime);
	
			let planTime = this.divMake('planTime',days.PLANTIME);
			workStick.appendChild(planTime);

			stick.appendChild(workStick);


			if(i>0 && i%14 == 0){
				stickBox.appendChild(stick);
				let stick = this.divMake('stick',99);
			}
		}
	
		// if(array.length%14 != 0){
		// 	stick.appendChild(workStick);
		// }

		stickBox.appendChild(stick);
	}		

	//div作成関数///
	divMake = function(divName,Time){


		let div = document.createElement("div");
		div.className= divName;

		if(Time==0){
			//0の時にはdivを作成しない
			div.style.height = "auto";
			div.textContent = "REST";
		}
		else if(Time!=99){
			//99:class=stick(親要素)の時には不要な要素
			//分で計算した値を時間数として扱う
			let time = this.T2t(Time);
			div.textContent = time;
			div.style.height = time*10 + "px";
		}
		return div;
	}

	//分単位を時間数に変換 90→1.5
	T2t = function(TIME){
		let time =Math.floor(TIME/60*100)/100;
		return time
	}
  

}




goStick.addEventListener('click',()=>{
	// クリック時にデータを取得
	data = timeInput.value;
	// let inputTimeEditer1 = new inputTimeEditer(timeInput);
	let inputTimeEditer1 = new stickModule(timeInput);
	inputTimeEditer1.makeStick();





	//Stick1.resetValue();
	//Stick1.addValue();
});


/*
10:10-17:20
10:30-20:50

10:00-15:00
10:00-20:00

10:10-17:20
10:30-20:50

x
x

10:00-15:00
10:00-20:00

10:10-17:20
10:30-20:50

x
x

10:00-15:00
10:00-20:00

file:///C:/Users/uemura/git/stick/index.html

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



todo 

	*divmakeは外でclassを作って作成
		じゃないと二度押しされたときに無限にstickが作成されてしまう
		一週間分作成するときを想定したときに無駄が多くなる気がする
		7日で改行させるのもこのクラスが受け持つ想定
	*weekのclassも作成
		day関数の方を繰り返し呼び出すもの
		一週間での計算を比較して時間外を計算する
	*monthのclassも作成
		一か月での計算を比較して時間外を計算する
		シンプルになる想定


*/