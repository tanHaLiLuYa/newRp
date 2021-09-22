const customName = document.getElementById('customname'); //输入自定义的名字”文本框的引用
const randomize = document.querySelector('.randomize'); //随机生成笑话”按钮的引用
const story = document.querySelector('.story');

function randomValueFromArray(array) {
    return array[Math.floor(Math.random() * array.length)];
}


var storyText = '今天气温 34 摄氏度，inserta出去遛弯。 当走到insertb门前时， 突然就insertc。人们都惊呆了， 李雷全程目睹但并没有慌， 因为inserta是一个 130 公斤的胖子， 天气又辣么热。';

var insertX = ['怪兽威利', '大老爹', '圣诞老人'];

var insertY = ['肯德基', '迪士尼乐园', '白宫'];

var insertZ = ['自燃了', '在人行道化成了一坨泥', '变成一条鼻涕虫爬走了'];



randomize.addEventListener('click', result);

function result() {
    let newStory, xItem, yItem, zItem, name;
    newStory = storyText;
    xItem = randomValueFromArray(insertX);
    yItem = randomValueFromArray(insertY);
    zItem = randomValueFromArray(insertZ);
    newStory = newStory.replace("inserta", xItem);
    newStory = newStory.replace("inserta", xItem);
    newStory = newStory.replace("insertb", yItem);
    newStory = newStory.replace("insertc", zItem);
    if (customName.value !== '') {
        name = customName.value;
        newStory = newStory.replace("李雷", name);
    }


    if (document.getElementById("american").checked) {
        let weight = Math.round(300) + "磅";
        let temperature = Math.round(94) + "开尔";
        newStory = newStory.replace("34 摄氏度", temperature);
        newStory = newStory.replace("130 公斤", weight)

    }

    story.textContent = newStory;
    story.style.visibility = 'visible';
}