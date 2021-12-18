let size = 100;

var world = new Array(size);
for(var y = 0; y<size;y++){
  world[y] = new Array(size);
}

function mod(n, m) {
  return ((n % m) + m) % m;
}

function setup() {
  for(var y = 0; y<size;y++){
    for(var x = 0; x<size;x++){
      world[y][x] = random(0, 1);
    }
  }

  createCanvas(size, size);
  
}


function get_nbs(x,y){
  return  world[mod(x-1,size)][mod(y-1,size)] + world[mod(x,size)][mod(y-1,size)] + world[mod(x+1,size)][mod(y-1,size)] + world[mod(x-1,size)][mod(y,size)] + world[mod(x+1,size)][mod(y,size)] + world[mod(x-1,size)][mod(y+1,size)] + world[mod(x,size)][mod(y+1,size)] + world[mod(x+1,size)][mod(y+1,size)];
}

let threshold = 4;

function draw() {
  let fw = new Array(size);
  for(let z = 0; z<size;z++){
    fw[z] = new Array(size);
  }

  for(let y = 0; y<size;y++){
    for(let x = 0; x<size;x++){
      let n = world[x][y];

 
      let nbs = get_nbs(x,y)/8;

      let newval = n/1.06;

      if(nbs < 2){
        newval *= 1 + nbs/8;
      }
      if(nbs > 7){
        newval /= 1+nbs/8;
      }

      fw[x][y] = newval;

      stroke(newval*255);
      point(x,y);

    }
  }
  world = fw;
  // console.log("updated!");
}