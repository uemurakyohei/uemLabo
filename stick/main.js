//documentからid属性がresultである要素を取得する
const timeInput = document.getElementById('timeInput');

//documentから「最大値」ボタン取得
const goStick = document.querySelector('#goStick button');

//inputの要素を格納
var data;

//documentからid属性がstickBoxである要素を取得する
const resultBox = document.getElementById('resultBox');

//作成した棒グラフの数を数える
let classCount = 0;

/////////////////
//時間の加工//////timeInput(~)→array[p1,w1,p2,w2...]
/////////////////
class inputTimeEditer{
	constructor(timeInput){
		//this.data = timeInput.value;		
		this.data = '\n\n10:00-18:00\n\n10:00-16:00\n\n10:00-18:00\n\n10:00-20:50\n\n10:00-15:00\n\n10:00-20:00\n\nx\n\nx\n\n10:00-17:30\n\n10:00-18:30\n\nx\n\n10:00-20:00\n\n10:00-17:30\n\n10:00-18:00\n\nx\n\nx\n\n10:00-17:30\n\n10:00-18:00';

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
//1日ごとの計算///day(planTime,workTime)→day.SHOTEIGAI,SHOTEINAI,JITSUDOU
/////////////////
class day{
	constructor(planTime,workTime){

		this.planTime = planTime;
		this.workTime = workTime;

		//実働、法定内、法定外
		this.SHOTEIGAI = 0;
		this.SHOTEINAI  = 0;
		this.JITSUDOU = 0;

		classCount +=1;
	}

	//値を定義する
	defineTime = function(){
		this.calcTime(this.planTime,this.workTime);
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
			//シフト時間が8h以下
			if (SHIFT <= 480){
				this.SHOTEINAI = 480 - SHIFT;
				this.SHOTEIGAI = TIME - 480;
				this.JITSUDOU = SHIFT;
			}
			//シフト時間が8h以上
			else{
				this.SHOTEIGAI = SHIFT - TIME;
				this.JITSUDOU = SHIFT;
			}
		}
		else{
			this.JITSUDOU = TIME;
		}
		console.log("shift",SHIFT);
		console.log("time",TIME);
		console.log("shotei",this.SHOTEINAI);
		console.log("shoteigai",this.SHOTEIGAI);
		console.log("plantime",this.JITSUDOU);
	}

	//静的メソッドで呼び出し可能:day.count()
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
//1週ごとの計算///week(planTimeW,workTimeW)→week.SHOTEIGAI,SHOTEINAI,PLANTIME
/////////////////
class week{
	constructor(planTimeW,workTimeW){
		//一週間分の所定時間と実働時間
		this.planTime = planTimeW;
		this.workTime = workTimeW;

		//実働、法定内、法定外
		this.SHOTEIGAI = 0;
		this.SHOTEINAI = 0;
		this.PLANTIME  = 0;


	}

	//値を定義する
	defineTime = function(){
		this.calcTime(this.planTime,this.workTime);
	}


	//一週間分の所定時間を40hと比較し実働時間から週の所定外時間を計算
	calcTime = function(p,w){
		if(p > 40){
			this.PLANTIME = p;
			console.log("yesyesysesopopo")
		}else{
			this.PLANTIME = 40;
			console.log("nononoopopop")
		}

		if(w > this.PLANTIME){
			this.SHOTEIGAI = w - this.PLANTIME;
			this.SHOTEINAI = this.PLANTIME;
			console.log("yesyesyses")
		}else{
			this.SHOTEIGAI = w;
			this.SHOTEINAI = 0;
			console.log("nonono")
		}
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

		//day classを使って日毎にインスタンスを作成
		//1日ごとの勤怠時間を計算
		for (let i = 0; i < array.length; i+=14) {

			let stickBox = this.divMakeDay('stickBox',99);

			//wwek用変数を定義
			let planTimeW = 0;
			let workTimeW = 0;

			for (let j = i; j < 14+i; j+=2) {



				let stick = this.divMakeDay('stick',99);

				//day class呼び出し
				let days = new day(array[j],array[j+1]);	
				days.defineTime();

				//格納データが無いときはdivを作らない
				if(days.planTime==null && days.workTime==null){
					break
				}

				let dayBox = this.divMakeDay('dayBox',99);


				//実働stick				
				let workStick = this.divMakeDay('workStick',99);

				let overTime = this.divMakeDay('overTime',days.SHOTEIGAI);
				workStick.appendChild(overTime);
				
				let outTime = this.divMakeDay('outTime',days.SHOTEINAI);
				workStick.appendChild(outTime);
				
				let jitsudou = this.divMakeDay('planTime',days.JITSUDOU);
				workStick.appendChild(jitsudou);

				//予定stick
				let planedStick = this.divMakeDay('planedStick',99);

				let overTimeP = this.divMakeDay('overTime',days.SHOTEIGAI);
				planedStick.appendChild(overTimeP);
				
				let outTimeP = this.divMakeDay('outTime',days.SHOTEINAI);
				planedStick.appendChild(outTimeP);
				
				let planTimeP = this.divMakeDay('planTime',days.planTime);
				planedStick.appendChild(planTimeP);



				stick.appendChild(planedStick);
				stick.appendChild(workStick);

				dayBox.appendChild(stick);

				//dayを入れる
				let dayNum = this.divMakeDay('day',day.count());
				dayBox.appendChild(dayNum);

				stickBox.appendChild(dayBox);


				//week用
				workTimeW += days.workTime;
				planTimeW += days.planTime;
	


			}

			//week class呼び出し
			let weeks = new week(planTimeW,workTimeW);	
			weeks.defineTime();
			
			let weekStick = this.divMakeWeek('weekStick',99);
			let weekPlan = this.divMakeWeek('weekPlan',weeks.PLANTIME);
			let weekWork = this.divMakeWeek('weekWork',99);

			let weekOut = this.divMakeWeek('weekOut',weeks.SHOTEINAI);
			let weekOver = this.divMakeWeek('weekOver',weeks.SHOTEIGAI);


			weekWork.appendChild(weekOut);
			weekWork.appendChild(weekOver);

			weekStick.appendChild(weekPlan);
			weekStick.appendChild(weekWork);

			console.log("week",planTimeW,workTimeW,weeks.PLANTIME,weeks.SHOTEINAI,weeks.SHOTEIGAI);


			resultBox.appendChild(stickBox);
			resultBox.appendChild(weekStick);
				
		}

	}		



	//div呼び出し関数



	//day用 div作成関数///
	divMakeDay = function(divName,Time){

		let div = document.createElement("div");
		div.className= divName;

		if(Time==0){
			//0の時にはdivを作成しない
			div.style.height = 0;
			div.textContent = "";
		}
		else if(divName=='day'){
			div.textContent = "day" + Time;			
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
  
	//week用 div作成関数///
	divMakeWeek = function(divName,Time){

		let div = document.createElement("div");
		div.className= divName;

		if(Time==0){
			//0の時にはdivを作成しない
			div.style.width = 0;
			div.textContent = "";
		}
		
		else if(Time!=99){
			//99:class=stick(親要素)の時には不要な要素
			//分で計算した値を時間数として扱う
			let time = this.T2t(Time);
			div.textContent = time;
			div.style.width = time*8 + "px";
		}
		return div;
	}

}




goStick.addEventListener('click',()=>{

	// クリック時にデータを取得
	data = timeInput.value;
	// let inputTimeEditer1 = new inputTimeEditer(timeInput);
	let inputTimeEditer1 = new stickModule(timeInput);
	inputTimeEditer1.makeStick();

	console.log("カウント",day.count());




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

	*divmakeDayは外でclassを作って作成
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