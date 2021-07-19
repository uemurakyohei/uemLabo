//documentからid属性がresultである要素を取得する
const p = document.getElementById('result');

//documentからtextarea要素を探し、最初に見つかった要素を取得する
const textarea = document.querySelector('textarea');


//documentからtype属性がradioであるinput要素を格納する
const radios = document.querySelectorAll('input[type="radio"]');

//documentから「変換する」ボタン取得
const convertButton = document.querySelector('#convert button');

//documentから「最大値」ボタン取得
const maxButton = document.querySelector('#max button');

let textRow;
let textRow2;

let num=0;

//カンマの数取得
// function numberComma(textRow){
//     const textLen = textRow.length;
//     for (let i=0; i < textLen;i++){
//         if(textRow[i]===','){
//             num ++;
//         }
//     }
//     return num;
// }

let changedRow;
//method（改行、タブ、カンマ） textの値から配列、配列数取得
function numberFunc(method,text){
    this.methods = method;
    this.text = text;


    // this.row = function(){
    //     textRow = this.text.split(this.methods);
    //     console.log(textRow)
    //     return textRow;
    // }

    this.row = function(){
        textRow = text.split(/[\n,\t]/);
        return textRow;
    }

    this.num = function(){
        textNum = textRow.length;
        return textNum;
    }

    this.changeRow = function(){
        const textLen = textRow.length;
        changedRow = textRow.join(this.methods);
        // for (let i=0; i < textLen;i++){
        //     changedRow.push(textRow[i]);
        //     changedRow.push(this.methods);
        // }
       return changedRow;
//        console.log(changedRow);
    }
    
 
}




let maxNum = 0;
function numberMax(text){
    textRow = text.split(/[\n,\t]/);

    console.log(textRow);
    textNum = textRow.map(Number);
    for (let i =0; i<textRow.length;i++){
        if( maxNum < textNum[i]){
            maxNum = textNum[i];
            console.log(typeof(maxNum));
        }
    }
    return maxNum;
}









convertButton.addEventListener('click',()=>{


    for (let i = 0; i < radios.length;i++){
        if (radios.item(i).checked){
            value = radios.item(i).value;
            break;
        }
        
    }
    console.log(value);
    textRow = textarea.value;
    var numberComm = new numberFunc(value,textRow);
    numberComm.row();
    numberComm.num();
    numberComm.changeRow();

    textarea.value = changedRow;

});



maxButton.addEventListener('click',()=>{
    textRow = textarea.value;

    numberMax(textRow);

    console.log(maxNum);
    p.textContent = maxNum;
});

