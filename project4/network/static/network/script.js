

  window.addEventListener("load", function(){
    checkthis = window.location.href;
    checkthissub = checkthis.split("/")[3];


    if (checkthis === "http://127.0.0.1:8000/" || checkthissub === "viewuser") {
      //follow button section

      if (document.getElementById('follow') != null){
      var vuserid = document.getElementById('follow').value;
      var followbtn = document.querySelector('#follow');
      followbtn.addEventListener('click', function follow(){
        fetch('/follow/'+vuserid, {
          method: 'PUT',
          body: JSON.stringify({
          user: "following"
        })
      }).then(response => response.json())
      .then(data => { location.reload();})
      ;}) }

      ///create button section
     const  createbtn = document.getElementById('newpost');
     if (createbtn != null){
     createbtn.addEventListener('click',
     function newpost() {
     check = document.querySelector('#inputcontainer')
      if (check === null){
      createbtn.style.display = "none";
      const input = document.createElement("textarea");
      input.setAttribute("type", "text");
      input.setAttribute("id", "postinput");
      input.setAttribute("rows", "4")
      input.style.width = "60vw";
      const inputcontainer = document.createElement("div");
      const y = document.createElement("button");
      y.innerHTML = "Submit";
      y.addEventListener('click', function post() {
        var posttext = document.querySelector('#postinput').value;

        // submit post to Database
        fetch('/newpost', {
          method: 'POST',
          body: JSON.stringify({
          newpost: posttext
        })
      }).then(response => response.json())
      .then(data => { if (data.status === "true"){ location.reload();}})



      })

      inputcontainer.setAttribute("id", "inputcontainer");
      inputcontainer.prepend(y);
      inputcontainer.prepend(input);
      document.querySelector('#postcontainer').prepend(inputcontainer);

      }
    });
  }
    }

if (checkthis === "http://127.0.0.1:8000/" || checkthissub === "viewuser" || checkthissub === "public" || checkthissub === "following") {

  document.getElementsByName('comment_text').forEach(item => {
    var c_id = item.id.split("/").pop();
    item.addEventListener('click', function(){
      var comment_input = this;
      if (comment_input.rows === 6) {return};
      var submit_button = document.createElement("button");
      submit_button.addEventListener('mousedown', function() {
              var comment_text = document.getElementById('new_comment/'+ c_id).value;
              fetch('/update/'+c_id, {
                method: 'PUT',
                body: JSON.stringify({
                commented: comment_text,
              })
            }).then(response => response.json())
            .then(data => { if (data.status === "true"){
              comment_input.value = "";
              var comment_sec = document.getElementById('comment_sec/'+c_id);
              var new_comment = document.createElement("div");
              new_comment.innerHTML = comment_text;
              comment_sec.append(new_comment);
            }});
          });
      submit_button.innerHTML = "Submit Comment";
      submit_button.id = "subtn";
      var parent = this.parentNode;
      parent.append(submit_button);
      comment_input.rows = 6;
      comment_input.focus();
      comment_input.setSelectionRange(0,0);
      comment_input.addEventListener('focusout', function (){
            var smbtn = document.getElementById("subtn");
            if (smbtn != null){
                smbtn.remove();
            };
            comment_input.rows = 1;

})
})
})

document.querySelectorAll(".see_comments").forEach(item => {
  item.addEventListener('click', function(){
    var commentbtn = this;
    const post_id = commentbtn.id.split("/").pop();
    var comment_count = 0;
    fetch('/update/'+post_id, {
      method: 'GET',
  }).then(response => response.json())
  .then(data => {
    var comment_sec = document.getElementById('comment_sec/'+post_id);
    comments_text = data;
    for (i = 0; i < comments_text.length; i++) {
      var new_comment = document.createElement("p")
      new_comment.innerHTML = comments_text[i].usersname+"|"+comments_text[i].text+"<br>"+comments_text[i].time;
      comment_sec.append(new_comment);
    }
  });// end of last then response
  commentbtn.style.visibility = "hidden";
})//end of event listener
});



document.querySelectorAll('.editbtn').forEach(item => {
  item.addEventListener('click', function(){
    var updated = function updated(editableText, postKepper, newText) {
      postKepper.innerHTML = newText;
      editableText.replaceWith(postKepper);

      fetch('/update/'+post_id, {
        method: 'PUT',
        body: JSON.stringify({
        edit: newText
      })
    }).then(response => response.json())
      .then(data => { if (data.status === "true"){
      console.log("successful");
    }//end of if statment
  })

  };
        var editbtn = this;
        var post_id = editbtn.id.split("/").pop();
        var post_text = document.getElementById(['text/'+post_id]);
        var postKepper = post_text.cloneNode();
        var editableText = document.createElement("textarea");

        editableText.value = post_text.innerHTML;
        editableText.id = 'cEditText';
        post_text.replaceWith(editableText);
        editableText.focus();
        editableText.setSelectionRange(0,0);
        editableText.addEventListener('blur', function (){
        var newText = editableText.value;
      if (event.target.id === 'cEditText'){ updated(editableText, postKepper, newText) ;}});
  })
});

  document.querySelectorAll('.likebtn').forEach(item => {
    item.addEventListener('click', function(){
      post_id = this.id.split("/").pop()
      update = this.innerHTML.split("</i>").pop();
      var regExp = /\(([^)]+)\)/;
      var matches = regExp.exec(update);
      const thumbs_up_icon = '<i style="font-size:24px" class="fa">&#xf087;</i>'
      const thumbs_down_icon = '<i style="font-size:24px" class="fa">&#xf165;</i>'
      // update like button
      fetch('/update/'+post_id, {
        method: 'PUT',
        body: JSON.stringify({
        like: "true"
      })
    }).then(response => response.json())
    .then(data => { if (data.status === "true"){
      like_count = matches[1] =+ 1;
      this.innerHTML = thumbs_up_icon + "("+like_count+")";
     }//end of if statment
    else if (data.status === "false") {
      like_count = matches[1] =- 1;
      if (like_count < 0){ like_count = 0;}
      this.innerHTML = thumbs_up_icon + "("+like_count+")";

    }
    else if (data.status === "2true") {
      like_count = matches[1] =+ 1;
      this.innerHTML = thumbs_up_icon + "("+like_count+")";
      update_likes = document.getElementById("unlike/"+post_id)
      u_likes_count = update_likes.innerHTML.split("</i>").pop();
      var n_matches = regExp.exec(u_likes_count);
      n_like_count = n_matches[1] =- 1;
      if (n_like_count < 0){ like_count = 0;}
      update_likes.innerHTML = thumbs_down_icon + "("+like_count+")";
    } // end of else
    });// end of last then response


    })
  });


  document.querySelectorAll('.dislikebtn').forEach(item => {
    item.addEventListener('click', function(){
      var post_id = this.id.split("/").pop()
      update = this.innerHTML.split("</i>").pop();
      var regExp = /\(([^)]+)\)/;
      var matches = regExp.exec(update);
      const thumbs_down_icon = '<i style="font-size:24px" class="fa">&#xf165;</i>'
      const thumbs_up_icon = '<i style="font-size:24px" class="fa">&#xf087;</i>'
      // update like button
      fetch('/update/'+post_id, {
        method: 'PUT',
        body: JSON.stringify({
        dislike: "true"
      })
    }).then(response => response.json())
    .then(data => { if (data.status === "true"){
      like_count = matches[1] =+ 1;
      this.innerHTML = thumbs_down_icon + "("+like_count+")";
     }//end of if statment
    else if (data.status === "false") {
      like_count = matches[1] =- 1;
      if (like_count < 0){ like_count = 0;}
      this.innerHTML = thumbs_down_icon + "("+like_count+")";

    }
    else if (data.status === "2true") {
      like_count = matches[1] =+ 1;
      this.innerHTML = thumbs_down_icon + "("+like_count+")";
      update_likes = document.getElementById("like/"+post_id)
      u_likes_count = update_likes.innerHTML.split("</i>").pop();
      var n_matches = regExp.exec(u_likes_count);
      n_like_count = n_matches[1] =- 1;
      if (n_like_count < 0){ like_count = 0;}
      update_likes.innerHTML = thumbs_up_icon + "("+like_count+")";

    }// end of else
    });// end of last then response
    })
  });//end of query seletor all
} //end of check if view has post



}

)
