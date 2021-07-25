document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);


  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#viewmail').style.display = 'none';
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
  document.querySelector('#compose-subject').setAttribute("placeholder", "Subject");
  document.querySelector('#compose-recipients').setAttribute("placeholder", "recipient");
  document.querySelector('#compose-form').addEventListener('submit', send_mail);
}

function send_mail() {
event.preventDefault()
var sendRecipient = document.querySelector('#compose-recipients').value;
var sendSubject = document.querySelector('#compose-subject').value;
var sendMessage = document.querySelector('#compose-body').value;
console.log(sendRecipient)
fetch("/emails", {
  method: 'POST',
  body: JSON.stringify({
      'recipients': sendRecipient,
      'subject': sendSubject,
      'body': sendMessage,
  })
})
.then(response => response.json())
.then(data => {
    // Print result
  let checkalert = document.querySelector('#alertstatus');
if (checkalert != null) {
  if ( data.message === "Email sent successfully." )
  {
    document.querySelector('#compose-form').style.pointerEvents = "none";
    document.querySelector('#alertstatus').style.backgroundColor = "#1fc344";
    document.querySelector('#alertstatus').style.color = "#000000";
    setTimeout( function () {location.reload();}, 3000);
  }
  document.querySelector('#alertstatus').style.backgroundColor = "#ea0505";
  document.querySelector('#alertstatus').style.color = "#fff";
  document.querySelector('#alertstatus').innerHTML = data.message;
} else {
  let sentstatus = document.createElement('div');
  sentstatus.setAttribute("id", "alertstatus");
  sentstatus.innerHTML = data.message;



    if ( data.message === "Email sent successfully." )
    {
      document.querySelector('#compose-form').style.pointerEvents = "none";
      sentstatus.setAttribute("class", "alertsuccess" )
      setTimeout( function () {location.reload();}, 3000);
    }
    else {
      sentstatus.setAttribute("class", "alerterror" );
    }

    document.querySelector('#compose-view').prepend(sentstatus);
}});

}

function mail_time(emailtime) {

  let etime = emailtime.timestamp.split('T').pop().split('Z')[0];
  etime = etime.split(':', 2);
  let thour = etime[0];
  let tminute = etime[1];
  if (thour > 12) {
    thour = thour - 12;
    if (thour < 10){
    var finaltime = "0"+thour+':'+tminute+'pm';
    }
    else { var finaltime = thour+':'+tminute+'pm'; }

  }
  else {
    var finaltime = thour+':'+tminute+'am';

  }

  return finaltime
}

function mail_date(emaildate) {

  return emaildate.timestamp.split('T', 2)[0];

}


function load_mailbox(mailbox) {
  document.querySelector('#inboxc').innerHTML = "";
  document.querySelector('#viewmail').innerHTML = "";
  document.querySelector('#viewmail').style.display = 'block';
  fetch("/emails/"+mailbox)
.then(response => response.json())
.then(data => {
    // Print emails
    console.log(data);
    data.forEach(display_mail);

function display_mail(item){
    //  clear mail view

    // ... create new elements for each email
    const element = document.createElement('div');
    const elementheader = document.createElement('h4');
    const elementbody = document.createElement('p');
    const elementsender = document.createElement('div');
    const elementtime = document.createElement('span');
    const emaildate = document.createElement('div');

    // set element class
    elementheader.setAttribute("class", "title" );
    elementbody.setAttribute("class", "preview" );
    elementtime.setAttribute("class", "timestamp" );
    element.setAttribute("class", "email" );
    elementsender.setAttribute("class", "sender" );
    emaildate.style.color = "#000000";


    if (item.read === true) {
      elementbody.style.backgroundColor = "lightgray";
      element.style.backgroundColor = "rgb(62 119 170)";
    };

    // input info from each email
    if (mailbox === "sent") {elementsender.innerHTML = item.recipients;}
    else {
      elementsender.innerHTML = item.sender;
    }
    elementtime.innerHTML = mail_time(item);
    emaildate.innerHTML = mail_date(item);
    if (item.subject === "") {
      elementheader.innerHTML = "No Subject";
    }
    else { elementheader.innerHTML = item.subject; }

    elementbody.innerHTML = item.body;
    element.addEventListener('click', function viewmail() {
      element.setAttribute("id", "currentemail");
      element.style.height = "fit-content";
      document.querySelector('#viewmail').innerHTML = "";
        // hide the current view... list of emails
        document.querySelector('#emails-view').style.display = 'none';
        // create email view buttons
        const archive = document.createElement('button');
        const reply = document.createElement('button');
        const mdelete = document.createElement('button');
        // set button name
        archive.innerHTML = "ARCHIVE";
        reply.innerHTML = "REPLY";
        mdelete.innerHTML = "DELETE";
        archive.setAttribute("name", "archive" );

        // add button style
        archive.setAttribute("class", "mailbuttons" );
        reply.setAttribute("class", "mailbuttons" );
        mdelete.setAttribute("class", "mailbuttons" );

        // add Event Listener for each button
        archive.addEventListener('click',function (){
          archivebutton = document.getElementsByName("archive")[0];
          if (archivebutton.innerHTML === "ARCHIVE"){
            archivebutton.setAttribute("class", "archived" );
            archivebutton.innerHTML = "ARCHIVED";
            function archived(){
              fetch('/emails/'+item.id, {
                  method: 'PUT',
                  body: JSON.stringify({
                  archived: "true"
                  })
                }) };
                archived();


          }
          else {
            archivebutton.setAttribute("class", "mailbuttons" );
            archivebutton.innerHTML = "ARCHIVE";
            function archive(){
              fetch('/emails/'+item.id, {
                  method: 'PUT',
                  body: JSON.stringify({
                  archived: false
                  })
                }) };
                archive();

        }} );
        reply.addEventListener('click', function (){
        compose_email();
        replytime = mail_time(item);
        document.querySelector('#compose-body').value = "\n\n\n\n\n\n"+"******"+item.sender+" @ "+emaildate.innerHTML+" "+replytime+"******"+"\n\n"+item.body;
        document.querySelector('#compose-recipients').value = item.sender;
        document.querySelector('#compose-subject').value = "re:"+item.subject;
        document.querySelector('#compose-body').focus();
        document.querySelector('#compose-body').setSelectionRange(0,0);
        document.querySelector('#compose-view').style.paddingTop = "110px";
        document.querySelector('#compose-body').scrollTo(0,0);

        });
        mdelete.addEventListener('click', function (){

          fetch('/emails/'+item.id, {
            method: 'PUT',
            body: JSON.stringify({
            deleted: true
            })
          })
          .then(response => {
            if (response.status === 204){
                document.querySelector('#currentemail').style.display = "none";
                let sentstatus = document.createElement('div');
                sentstatus.setAttribute("class", "alertsuccess" );
                sentstatus.innerHTML = "Email successfully deleted.";
                document.querySelector('#viewmail').append(sentstatus);
                setTimeout( function () {location.reload();}, 3000);
            }
            else { let sentstatus = document.createElement('div');
            sentstatus.setAttribute("class", "error" );
            sentstatus.innerHTML = "Error could not delete email.";}
            document.querySelector('#viewmail').append(sentstatus);
            setTimeout( function () {location.reload();}, 3000);
          })
      });

        // add to email view
        document.querySelector('#viewmail').append(element);
        if (document.querySelector('#secname').innerHTML === "<h3>Sent</h3>") {
          elementsender.innerHTML = item.recipients;
          element.append(mdelete);
        } else {
          element.append(archive);
          element.append(reply);
          element.append(mdelete);
        }


        // mark email as read
        fetch('/emails/'+item.id, {
          method: 'PUT',
          body: JSON.stringify({
          read: true
        })
      })
      // if conditions

      if (item.archived === true){
        archive.setAttribute("class", "archived" );
        archive.innerHTML = "ARCHIVED";
      }
      // Last event. Remove the event listener from email element
    element.removeEventListener('click', viewmail);

    });
    elementtime.append(emaildate);
    element.append(elementtime);
    element.append(elementheader);
    element.append(elementsender);
    element.append(elementbody);



    document.querySelector('#inboxc').append(element);
}
});

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  upTitle = document.querySelector('#secname')
  upTitle.innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  upTitle.style.position = "fixed";
  upTitle.style.backgroundColor = "#fff";
  upTitle.style.width = "80.8vw";
  upTitle.style.textAlign = "center";

}
