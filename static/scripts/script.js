var inputElement = document.getElementById("Newtask");
var count = 0

function addd(){
    var start = document.getElementById('Start-day');
    var end = document.getElementById('End-day');
    if (inputElement.value == "" ){
        window.alert('pls write something');
        return;
    }
    if(start.value==='' || end.value===''){
        window.alert('Please enter start-day and end-day');
        return;
    }
    if(start.value>end.value){
        end.value=start.value
    }
    
    else{
        
        const tr = document.createElement("tr");
        count += 1;
        tr.id = count;
        tr.innerHTML=`
        <td><h4>${count}</h4></td>
        <td><input type="checkbox" id="Todo1" onchange="checkcomplete(this)"></td>
        <td><label for="Todo1">${inputElement.value}</label></td>
        <td>${start.value}</td>
        <td>${end.value}</td>
        <td><span id = "Status">Incomplete</span></td>
        <td><button onclick="deletetask(${count})">
                <span class="material-symbols-outlined">
                    delete
                </span>
            </button>
        </td>
        <td><button onclick="editTask(${count})">
            <span class="material-symbols-outlined">
                edit
                </span>
            </button>
        </td>`
        
        document.getElementById("taskList").appendChild(tr);
        inputElement.value='';
        start.value='';
        end.value='';
    } 
   
}
function checkcomplete(checkbox){
    var s = checkbox.parentNode.parentNode;
    var Stat = document.getElementById('Status'); 
    if(checkbox.checked){
        s.setAttribute('style', 'background-color:green;');
        Stat.textContent="Completed";
    }
    else{
        s.setAttribute('style', 'background-color:white;');
        Stat.textContent="Incomplete"; 
    }

}
function deletetask(taskId){
    var bruh = document.getElementById(taskId);
    if(bruh){
        bruh.parentNode.removeChild(bruh);
    } else{
        window.alert('Id not found');
    }
}
// function edit(taskId){
//     var task=document.getElementById(taskId);
//     if(task){
//     var labelElement = task.querySelector('label');
//     var startElement = task.querySelector('td:nth-child(4)');
//     var endElement = task.querySelector('td:nth-child(5)');
//     var newTask = prompt('Enter new task:');
//     var newStart = prompt('Enter new Start day:');
//     var newEnd = prompt('Enter new End day:');
//     labelElement.textContent=newTask;
//     startElement.textContent=newStart;
//     endElement.textContent=newEnd;}
    
// }
function editTask(taskId){
    var taskToEdit = document.getElementById(taskId);
    var taskInput = document.getElementById('Newtask');
    var start = document.getElementById('Start-day');
    var end = document.getElementById('End-day');
    var td = taskToEdit.getElementsByTagName('td');

    taskInput.value=td[2].textContent;
    start.value=td[3].textContent;
    end.value = td[4].textContent;

    var addButton = document.getElementById('Add');
    addButton.textContent='Update';

    addButton.onclick = function(){
        saveChanges(taskId);
    };
}
function saveChanges(taskId){
    var taskToEdit = document.getElementById(taskId);
    var taskInput = document.getElementById('Newtask');
    var start = document.getElementById('Start-day');
    var end = document.getElementById('End-day');
    var td = taskToEdit.getElementsByTagName('td');

    if(start.value>end.value){
        end.value=start.value
    }

    td[2].textContent = taskInput.value;
    td[3].textContent = start.value;
    td[4].textContent = end.value;

    var addButton = document.getElementById('Add');
    addButton.textContent='Add';
    
    addButton.onclick = addd;
    
    taskInput.value='';
    start.value='';
    end.value='';
}