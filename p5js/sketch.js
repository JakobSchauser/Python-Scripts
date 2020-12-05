let size = 400;
let gridsize = size/9;
let inputvalue = 0; 

let board = [];
let possibles = []

function setup() {
  createCanvas(size, size);
  for(var i=0;i<9;i++){
    board[i] = [];
    for(var j=0;j<9;j++){
      board[i][j] = 0;
  }}
  for(var i=0;i<=9;i++){
    possibles[i] = [];
    for(var j=0;j<=9;j++){
      possibles[i][j] = [];
      for(var k=1;k<=9;k++){
        possibles[i][j][k-1] = k;
      }
  }}
}

function draw() {
  
  background(220);
  draw_board();
  xy = snap(mouseX,mouseY);
  text(str(inputvalue),xy[0],xy[1]);
  for(var i=0;i<9;i++){
    for(var j=0;j<9;j++){
      var val = board[i][j];
      xy = gridtoworld(i,j);
      
      if(val!=0){
        text(str(val),xy[0],xy[1]);

      }
    }}
}

function draw_board(){
  for(var i=0;i<=9;i++){
    strokeWeight(1);

    if(i%3==0){
      strokeWeight(3);
    }
    var x = i*size/9;
    var y = i*size/9;
    line(x,0,x,size);
    line(0,y,size,y);
  }
}
function worldtogrid(x,y){
  return [floor(x/size*9),floor(y/size*9)];
}
function gridtoworld(x,y){
  return [x*gridsize+gridsize/2,y*gridsize+gridsize/2];
}
function snap(x,y){
  var xy = worldtogrid(x,y);
  return gridtoworld(xy[0],xy[1]);
}

function keyPressed() {
  if (keyCode>47 && keyCode<58) {
    inputvalue = keyCode-48;
  }
  if(keyCode==13){
    var solution = solveBoard(board)
  }
}
function mouseClicked() {
  ij = worldtogrid(mouseX,mouseY);
  board[ij[0]][ij[1]] = inputvalue;
  if(inputvalue == 0){
    possibles[ij[0]][ij[1]] = [1,2,3,4,5,6,7,8,9]
  } else {
    possibles[ij[0]][ij[1]] = [0]
  }
  
} 

function solveBoard(board){
  let l = 9;
  print("Solve!")
  for(let y = 0;y<l;y++){
    for(let x = 0;x<l;x++){
      if(board[x][y]!=0){
        continue;
      }
      //Find row and coloumn
      var column = board[x];
      var row = board.map(x => x[y]);

      // find local square
      let tile = []
      var sx = int(Math.floor(x/3)*3);
      var sy = int(Math.floor(y/3)*3);
      for(let xx=sx;xx<sx+3;xx++){
        for(let yy=sy;yy<sy+3;yy++){
          tile.push(board[xx][yy]);
        }
      }

      let comb = [];
      comb.push(column,row,tile);
      comb = comb.join().split(",");

      var number;
      for (number in comb){
        if(number == 0){
          continue;
        }
        print(number);
        print(possibles[x][y]);
        contains = possibles[x][y].includes(number);
        print(contains);
        return

        if(contains){
          print(number)
          for( var i = 0; i < possibles[x][y].length; i++){ 
            if ( possibles[x][y][i] === number) { possibles[x][y].splice(i, 1); }
          }
        }
      }

      if(possibles[x][y].length==1){
        let pos = possibles[x][y][0];
        print("set!");
        if(pos!=0){
          
          board[x][y] = pos;
        }
      }

    }
  }
}