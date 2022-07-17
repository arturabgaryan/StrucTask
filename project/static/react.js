// После обновления Node на новую версию с импротом реакта возникла ошибка, я временно переписал код через Node,
// как только исправлю ошибку, верну реакт код


const add_button = document.querySelector('#add');
const form = document.querySelector('form');
const remove_button = document.querySelectorAll('.remove');

for(var i = 0;i<remove_button.length; i++){
    const elem = remove_button[i];
    elem.addEventListener('click', delet);
}


var counter = 0;

add_button.addEventListener('click', Func);


function Func(){
    counter++;

    options = {
        textContent:"New feature " + counter.toString(),
        className: 'lbl',
        id: 'label ' + counter.toString()
    }

    label = Object.assign(document.createElement('label'),options);

    inp = Object.assign(document.createElement('input'),{id: "input" + counter.toString(), name: "name " + counter.toString()});

    options = {
        className:'remove',
        textContent:'x',
        id:'remove' + counter.toString(),
        type: 'button'
    }

    remove = Object.assign(document.createElement('button'),options);
    remove.addEventListener('click',Del);

    br = Object.assign(document.createElement('br'),{id:'br ' + counter.toString()});
    br_2 = Object.assign(document.createElement('br'),{id:'br_2 ' + counter.toString()});
    br_3 = Object.assign(document.createElement('br'),{id:'br_3 ' + counter.toString()});
    br_4 = Object.assign(document.createElement('br'),{id:'br_4 ' + counter.toString()});
    br_5 = Object.assign(document.createElement('br'),{id:'br_5 ' + counter.toString()});
    br_6 = Object.assign(document.createElement('br'),{id:'br_6 ' + counter.toString()});
    br_7 = Object.assign(document.createElement('br'),{id:'br_7 ' + counter.toString()});
    br_8 = Object.assign(document.createElement('br'),{id:'br_8 ' + counter.toString()});

    select = Object.assign(document.createElement('select'),{id:'select ' + counter.toString(), name:'type ' + counter.toString()});

    option1 = Object.assign(document.createElement('option'),{textContent:'string'});
    option2 = Object.assign(document.createElement('option'),{textContent:'number'});
    option3 = Object.assign(document.createElement('option'),{textContent:'array'});

    select.append(option1);
    select.append(option2);
    select.append(option3);

    descrLabel = Object.assign(document.createElement('label'),{id: 'descrlabel ' + counter.toString(), textContent:'Default:'});
    descrInp = Object.assign(document.createElement('input'),{id: 'descrinput ' + counter.toString(), name:'descrinput ' + counter.toString()});

    descriptionLabel = Object.assign(document.createElement('label'),{id: 'description label ' + counter.toString(), textContent:'Description:'});
    description = Object.assign(document.createElement('input'),{id: "description " + counter.toString(), name:'description ' + counter.toString()});

    block = Object.assign(document.createElement('div'),{id: 'div ' + counter.toString()});

    block.append(label);
    block.append(remove);
    block.append(br);
    block.append(inp);
    block.append(br_2);
    block.append(select);
    block.append(br_3);
    block.append(descrLabel);
    block.append(br_4);
    block.append(descrInp);
    block.append(br_5);
    block.append(descriptionLabel);
    block.append(br_6);
    block.append(description);
    block.append(br_7);
    block.append(br_8);

    form.append(block);

}


function chName(val){
  const sel = document.getElementById(val);
  const label = document.getElementById('descrlabel ' + val.replace('select ',''));
  if (sel.value == 'number'){
   label.innerHTML = 'minimum';
  }
  else if (sel.value == 'array'){
   label.innerHTML = 'default';
  }
  else if (sel.value == 'string'){
   label.innerHTML = 'Default';
  }

}


function delet(){
    const id = this.id;
    const block = document.getElementById('div ' + id);

    block.remove();
}


function Del(){
 const Id = this.id;
 const block = document.getElementById('div ' + Id.slice(-1));

 block.remove();
}