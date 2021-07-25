

  window.addEventListener("load", function(){
    checkthis = window.location.href;
    checkthissub = checkthis.split("/")[3];
    checkthissub3 = checkthis.split("/")[5];
    var listnumber = 0 ;
    var clicked = 0;
    var listitems = [] ;
    if (checkthissub3 === "Items"){
      var list_item = document.getElementsByClassName('list_item');
      for (i = 0; i <list_item.length; i++){
        list_item[i].style.backgroundColor = "#4CAF50";
        list_item[i].style.color = "#fff";
        list_item[i].style.margin = "3px";
        list_item[i].onclick = function () {
          if (document.getElementsByClassName('c_select')[0]) {
            document.getElementsByClassName('c_select')[0].removeAttribute("class");
          }
          this.setAttribute("class", "c_select");
        }
      };



        function makeSelectable(billitem, upc) {
          billitem.onclick = function () {
            clicked++;
            if (clicked === 1) {
              delay_select = setTimeout(function() {
              var list = document.getElementsByClassName('selected');
              for (var i = 0; i < list.length; i++) {
                list[i].removeAttribute("class");
                }
                billitem.setAttribute("class", "selected");
                clicked = 0;
              }, 150);
            } else {
              Lookup(upc);
              clicked = 0;
           }
            }
        }


    }

    if (checkthissub3 === "Staff"){
      var list_item = document.getElementsByClassName('list_item');
      for (i = 0; i <list_item.length; i++){
        list_item[i].style.backgroundColor = "#4CAF50";
        list_item[i].style.color = "#fff";
        list_item[i].style.margin = "3px";
        list_item[i].onclick = function () {
          if (document.getElementsByClassName('c_select')[0]) {
            document.getElementsByClassName('c_select')[0].removeAttribute("class");
          }
          this.setAttribute("class", "c_select");
        }
      };



        function makeSelectable(billitem, upc) {
          billitem.onclick = function () {
            clicked++;
            if (clicked === 1) {
              delay_select = setTimeout(function() {
              var list = document.getElementsByClassName('selected');
              for (var i = 0; i < list.length; i++) {
                list[i].removeAttribute("class");
                }
                billitem.setAttribute("class", "selected");
                clicked = 0;
              }, 150);
            } else {
              Lookup(upc);
              clicked = 0;
           }
            }
        }


      document.getElementById('add_staff_btn').onclick = function () {
      document.getElementById('new_cashier_sec').style.display = "block";
      document.getElementById("lookup_t_x").onclick = function () {
      this.parentElement.parentElement.style.display = "none";
    }}
    document.getElementById("t_x").onclick = function () {
    this.parentElement.parentElement.style.display = "none";
  }
      document.getElementById("del_staff_btn").onclick = function () {
        if (document.getElementsByClassName("c_select")[0] != null) {
            selected = document.getElementsByClassName("c_select")[0];
            staff_id = selected.id.split('/').pop();
            user_info = selected.value.split('/');
            document.getElementById('con_delete').style.display = "block";
            document.getElementById('user_del').innerHTML = user_info[1]
             }
          }
      document.getElementById("t_xx").onclick = function () {
      this.parentElement.parentElement.style.display = "none";
        }
      document.getElementById("t_xxx").onclick = function () {
      this.parentElement.parentElement.style.display = "none";
        }

      document.getElementById('update_pin_btn').onclick =  function () {
          if (document.getElementById('password_pin').value === document.getElementById('password_confirmation').value) {
            fetch('/update_set/', {
              method: 'PUT',
              body: JSON.stringify({
                status: "update_pswd",
                staff_id: staff_id,
                pin: document.getElementById('password_pin').value
                })
              }).then(response => response.json())
              .then(data => {
                  // log response
                  console.log(data);
                  if (data.status === "successful") {
                    //Display Successful message
                    document.getElementById('success_msg').style.display = 'block';
                    document.getElementById('success_msg').innerHTML = "Pin Successfully Updated"
                    setTimeout( function () {
                      location.reload();
                    } , 3000 )
                  } else {
                    //Display error message
                    document.getElementById('warning_msg').style.display = 'block';
                    document.getElementById('warning_msg').innerHTML = "Could not update pin";
                    setTimeout( function () {
                      location.reload();
                    } , 3000 )
                  }
                })

          } else {
            document.getElementById('warning_msg').style.display = 'block';
            document.getElementById('warning_msg').innerHTML = "Pin and confirmation did not match"
            setTimeout( function () {
              document.getElementById('warning_msg').style.display = 'none';
            } , 3000 )
          }
      }

      document.getElementById('delete_user').onclick =  function () {
        if (document.getElementsByClassName("c_select")[0] != null) {
          selected = document.getElementsByClassName("c_select")[0];
          staff_id = selected.id.split('/').pop();

            fetch('/update_set/', {
              method: 'PUT',
              body: JSON.stringify({
                status: "delete_user",
                staff_id: staff_id
                })
              }).then(response => response.json())
              .then(data => {
                  // log response
                  console.log(data);
                  if (data.status === "successful") {
                    document.getElementById('success_msg').style.display = 'block';
                    document.getElementById('success_msg').innerHTML = "User deleted successfully";
                    setTimeout( function () {
                      location.reload();
                    } , 3000 )
                  } else {

                    //Display error message

                  }

                }) }
      }

      document.getElementById("edit_staff_btn").onclick = function () {
        if (document.getElementsByClassName("c_select")[0] != null) {
          selected = document.getElementsByClassName("c_select")[0];
          staff_id = selected.id.split('/').pop();
          user_info = selected.value.split('/');
          document.getElementById('update_username').value = user_info.pop();
          var months = {
            January:"01",
           February:"02",
           March:"03",
           April:"04",
           May:"05",
           June:"06",
           July:"07",
           August:"08",
           September:"09",
           October:"10",
           November:"11",
           December:"12",
          }
          date = user_info.pop().replace(",", "")
          date = date.split(' ').slice(2,3)+"-"+months[date.split(' ')[0]]+"-"+date.split(' ').slice(1,2);
          console.log(date);
          document.getElementById('update_dob').value = date;
          document.getElementById('update_position').value = user_info.pop();
          document.getElementById('update_email').value = user_info.pop();
          document.getElementById('update_lastname').value = user_info.pop();
          document.getElementById('update_firstname').value =user_info.pop();
          //show update user popup
          document.getElementById('update_sec').style.display = "block";

          document.getElementById('update_pin').addEventListener('click', function functionName() {
            document.getElementById('update_pw_sec').style.display = "block";

          })

          document.getElementById('update_btn').addEventListener('click', function functionName() {
            fetch('/update_set/', {
              method: 'PUT',
              body: JSON.stringify({
                status: "update_staff",
                staff_id: staff_id,
                firstname: document.getElementById('update_firstname').value,
                lastname: document.getElementById('update_lastname').value,
                position: document.getElementById('update_position').value,
                email: document.getElementById('update_email').value,
                dob: document.getElementById('update_dob').value,
                username: document.getElementById('update_username').value
                })
              }).then(response => response.json())
              .then(data => {
                  // log response
                  console.log(data);
                  if (data.status === "successful") {
                    //Display Successful message

                    location.reload();
                  } else {

                    //Display error message

                  }

                })
          })
        }
      }

    }

    if (checkthissub3 === "Inventory"){
      var list_item = document.getElementsByClassName('list_item');
      for (i = 0; i <list_item.length; i++){
        list_item[i].style.backgroundColor = "#4CAF50";
        list_item[i].style.color = "#fff";
        list_item[i].style.margin = "3px";
        list_item[i].onclick = function () {
          if (document.getElementsByClassName('c_select')[0]) {
            document.getElementsByClassName('c_select')[0].removeAttribute("class");
          }
          this.setAttribute("class", "c_select");
        }
      };



        function makeSelectable(billitem, upc) {
          billitem.onclick = function () {
            clicked++;
            if (clicked === 1) {
              delay_select = setTimeout(function() {
              var list = document.getElementsByClassName('selected');
              for (var i = 0; i < list.length; i++) {
                list[i].removeAttribute("class");
                }
                billitem.setAttribute("class", "selected");
                clicked = 0;
              }, 150);
            } else {
              Lookup(upc);
              clicked = 0;
           }
            }
        }



    }

    if (checkthissub3 === "Transactions"){

      document.getElementById('view_btn').onclick = function () {
        id = document.getElementsByClassName('c_select')[0].id.split('/').pop()
        reciept = document.getElementById('reciept/'+id)
        document.getElementById('reciept_lookup_sec').style.display = 'block';
        document.getElementById('results_sec').innerHTML = reciept.innerHTML;

      }

      document.getElementById('refund_btn').onclick = function () {
        var refund_total = 0;
        id = document.getElementsByClassName('c_select')[0].id.split('/').pop()
        reciept = document.getElementById('reciept/'+id)
        document.getElementById('reciept_lookup_sec').style.display = 'block';
        document.getElementById('results_sec').innerHTML = reciept.innerHTML;
        items = document.getElementById('item_bill_sec').children;
        addtag = document.createElement('div');
        addtag.classList.add('item_tag');
        addtag.innerHTML = "refund qty";
        tags = document.getElementById('item_model').children[2].children;
        document.getElementById('item_model').children[2].remove()
        for (var i = 0; i < tags.length; i++) {
          document.getElementById('item_model').append(tags[i]);
        }
        document.getElementById('item_model').append(addtag);
        document.getElementById('totals_sec').style.padding= "3px";
        document.getElementById('totals_sec').style.background = "thistle";
        document.getElementById('totals_sec').style.borderBottom = "1px solid black";
        document.getElementById('item_list').style.display = "contents";
        if (document.getElementById('results_sec').lastChild.id != 'full_refund' ) {
        refund_sec = document.createElement('div');
        refund_txt = document.createElement('h3');
        refund_amount = document.createElement('h3');
        refund_amount.id = 'refund_amount';
        refund_amount.style.color = "#7fff00";
        refund_txt.id = 'refund_txt';
        refund_txt.style.color = "white";
        refund_sec.id = 'refund_sec';
        refund_sec.classList.add('refund_sec');
        refund_txt.innerHTML = "Refund";
        refund_sec.append(refund_txt);
        refund_sec.append(refund_amount);
        refund_sec.onmousedown  = function () {
            refund_sec.style.boxShadow = "inset 2px 2px 2px 6px #e503e5";
          }
        refund_sec.onmouseup  = function () {
            confirm_x = document.createElement('div');
            confirm_x.id = "confirm_x";
            confirm_x.innerHTML = "&#215;";
            confirm_x.classList.add('lookup_x')
            confirm_refund = document.createElement('div');
            confirm_refund.id = "confirm_refund";
            confirm_refund.classList.add("confirm_refund");
            confirm_refund.append(confirm_x);
            confirm_refund.innerHTML = confirm_refund.innerHTML.concat("<h2>Confirm Refund</h2><br>Amount<br>"+refund_amount.innerHTML+"<br>");
            confirm_refund_btn = document.createElement('button');
            confirm_refund_btn.innerHTML = "CONFIRM";
            confirm_refund_btn.classList.add('btn-warning');
            confirm_refund_btn.onclick = function () {

              del_op = document.getElementsByName('options')
              while (document.getElementsByName('options')[0]) {
                document.getElementsByName('options')[0].remove();
              }
              var new_reciept = document.getElementById('results_sec').innerHTML;
              fetch("/update_set/", {
                method: 'PUT',
                body: JSON.stringify({ status:"new_reciept", t_id: id, reciept:new_reciept })
              }).then(response => response.json())
                .then(data => {
                    if (data.status == "successful") {
                      location.reload();
                    } else {
                      console.log("EORROR")
                      console.log(data.status);
                    } })
                  }

                confirm_refund.append(confirm_refund_btn);
                document.getElementById('reciept_lookup_sec').append(confirm_refund);
                document.getElementById('confirm_x').onclick = function () {
                  this.parentNode.parentNode.style.display = "none";
                  this.parentNode.remove()
                }
              if (document.getElementById('totals_sec').children.length != 4) {
                refund_total_sec = document.createElement('div');
                refund_total_sec.innerHTML = "REFUND TOTAL"
                refund_span = document.createElement('span');
                refund_span.style.float = "right";
                refund_span.id = "refund_span";
                refund_total_sec.append(refund_span);
                document.getElementById('totals_sec').append(refund_total_sec);
                last_refund_amount = 0;
              } else {
                last_refund_amount = parseFloat(document.getElementById('refund_span').innerHTML);
              }


              recal_input = document.getElementById('item_bill_sec').children;
              refund_sec.style.boxShadow = "0 0 20px rgb(0 0 0 / 80%)";

              for (var r = 0; r < recal_input.length; r++) {
                if (recal_input[r].style.textDecoration != "line-through" ) {

                  var old_item_qty = recal_input[r].children[4].innerHTML;

                    item_id = recal_input[r].children[0].innerHTML;
                    if (recal_input[r].children[5].value === old_item_qty) {
                      recal_input[r].style.textDecoration = "line-through";
                    }

                    if (recal_input[r].children[5].value > 0) {
                      var refund_input_amount = recal_input[r].children[5].value;
                      recal_input[r].innerHTML =  recal_input[r].innerHTML.concat(refund_input_amount*-1+"x")
                      recal_input[r].children[3].style.width = "17%";
                      document.getElementById('refund_span').innerHTML = (last_refund_amount + refund_total* -1).toFixed(2);
                    }


                }
              }
              var allitems = 0;
              for (var d = 0; d < items.length; d++) {
                if (items[d].style.textDecoration === "line-through") {
                  allitems++;
                }
                if (allitems === items.length) {
                  full_refund =  document.createElement('div');
                  full_refund.classList.add("full_refund");
                  full_refund.id = "full_refund"
                  full_refund.innerHTML = "FULLY REFUNDED";
                  document.getElementById('results_sec').append(full_refund)
                  refund_sec.remove()
                }
              }



            }
            if (document.getElementById('reciept_lookup_sec').children.length === 3) {
              document.getElementById('reciept_lookup_sec').append(refund_sec);
            }

}



        input_length = items.length - 1;
        for (var i = 0; i < items.length; i++) {
          item_qty = items[i].children[4].innerHTML;
          item_tax = parseFloat(items[i].children[3].innerHTML);
          item_price = items[i].children[2].innerHTML;
          refund_input = document.createElement('select');
          refund_input.name = "options"
          for (var j = 0; j <= item_qty.length; j++) {
            var option  = document.createElement('option')
            option.innerHTML = j;
            refund_input.append(option)
          }


          item_qty = refund_input.value ;
          refund_input.classList.add("refund_input");
          if (items[i].style.textDecoration != "line-through" && items[i].children.length < 6) {
            items[i].append(refund_input);
          }

          items[i].style.background = "thistle";
          items[i].style.borderBottom = "1px solid black";
          if (i === input_length && document.getElementById('results_sec').lastChild.id != "full_refund") {
                document.getElementById("refund_amount").innerHTML = "$"+refund_total.toFixed(2)* -1;
              }

          refund_input.onchange = function () {

            recal_item = this.parentElement;
            recal_item_qty = parseFloat(this.value);
            recal_item_tax = parseFloat(recal_item.children[3].innerHTML);
            recal_item_price = parseFloat(recal_item.children[2].innerHTML);
            var recal_taxrate = recal_item_tax * 0.01;
            var recal_itemtax = recal_item_qty * recal_item_price * recal_taxrate ;
            var recal_item_amount = recal_item_qty * recal_item_price + recal_itemtax;
            refund_total = refund_total + recal_item_amount ;
            document.getElementById("refund_amount").innerHTML = "$"+refund_total.toFixed(2)* -1;
            this.disabled = true;

              }

      }

      }

      document.getElementById('void_btn').onclick = function () {

      }

      document.getElementById("reciept_x").onclick = function () {
      this.parentElement.style.display = "none";
      document.getElementById('results_sec').innerHTML = "";
      if (document.getElementById('refund_amount') != null) {
        document.getElementById('refund_sec').remove();
      }
        }

        var list_item = document.getElementsByClassName('list_item');
        for (i = 0; i <list_item.length; i++){
          list_item[i].style.backgroundColor = "rgb(175 76 76)";
          if (list_item[i].children[6].innerHTML.search("FULLY REFUNDED") === -1) {
            list_item[i].style.backgroundColor = "rgb(204 198 20)";
          }
          if (list_item[i].children[5].innerHTML === "valid") {
            list_item[i].style.backgroundColor = "#4CAF50";
          }

          list_item[i].style.color = "#fff";
          list_item[i].style.margin = "3px";
          list_item[i].onclick = function () {
            if (document.getElementsByClassName('c_select')[0]) {
              document.getElementsByClassName('c_select')[0].classList.add("whiteline")
              document.getElementsByClassName('c_select')[0].classList.remove("c_select");
            }
            this.classList.add("c_select")
            this.classList.remove("whiteline")
          }
        };

        function makeSelectable(billitem, upc) {
          billitem.onclick = function () {
            clicked++;
            if (clicked === 1) {
              delay_select = setTimeout(function() {
              var list = document.getElementsByClassName('selected');
              for (var i = 0; i < list.length; i++) {
                list[i].removeAttribute("class");
                }
                billitem.setAttribute("class", "selected");
                clicked = 0;
              }, 150);
            } else {
              Lookup(upc);
              clicked = 0;
           }
            }
        }
    }




    if (checkthis === "http://127.0.0.1:8000/" || checkthissub === "pos") {
      const checkout_button = document.getElementById("checkout_button");

      var list_item = document.getElementsByClassName('list_item');
      for (i = 0; i <list_item.length; i++){
        list_item[i].style.backgroundColor = "#4CAF50";
        list_item[i].style.color = "#fff";
        list_item[i].style.margin = "3px";
        list_item[i].onclick = function () {
          if (document.getElementsByClassName('c_select')[0]) {
            document.getElementsByClassName('c_select')[0].removeAttribute("class");
          }
          this.setAttribute("class", "c_select");
        }
      };



        function makeSelectable(billitem, upc) {
          billitem.onclick = function () {
            clicked++;
            if (clicked === 1) {
              delay_select = setTimeout(function() {
              var list = document.getElementsByClassName('selected');
              for (var i = 0; i < list.length; i++) {
                list[i].removeAttribute("class");
                }
                billitem.setAttribute("class", "selected");
                clicked = 0;
              }, 150);
            } else {
              Lookup(upc);
              clicked = 0;
           }
            }
        }


      function sub_price(price, tax, amount) {
        var newprice = price * amount;
        var taxrate = tax * 0.01;
        var itemtax = newprice * taxrate;
        var itemtotal = newprice + itemtax;
        var total = document.getElementById("total").innerHTML - itemtotal;
        var taxtotal = document.getElementById("tax").innerHTML - itemtax;
        var subtotal = document.getElementById("subtotal").innerHTML - newprice;

        document.getElementById("subtotal").innerHTML = subtotal.toFixed(2);
        document.getElementById("tax").innerHTML = taxtotal.toFixed(2);
        document.getElementById("total").innerHTML = total.toFixed(2);
        checkout_button.innerHTML = "<div style='color:white'>$"+total.toFixed(2)+"</div>CHECK OUT";
      }
      function add_price(price, tax, amount){
        var subtotal = amount * price + parseFloat(document.getElementById("subtotal").innerHTML);
        var taxrate = tax * 0.01;
        var itemtax = amount * price * taxrate ;
        var taxtotal = parseFloat(document.getElementById("tax").innerHTML) + itemtax;
        var total = subtotal + taxtotal ;

        document.getElementById("subtotal").innerHTML = subtotal.toFixed(2);
        document.getElementById("tax").innerHTML = taxtotal.toFixed(2);
        document.getElementById("total").innerHTML = total.toFixed(2);
        checkout_button.innerHTML = "<div style='color:white'>$"+total.toFixed(2)+"</div>CHECK OUT";
        }

        function VoidReg(){
          document.getElementById("subtotal").innerHTML = "0";
          document.getElementById("total").innerHTML = "0";
          document.getElementById("tax").innerHTML = "0";
          document.getElementById('item_bill_sec').innerHTML = "";
          document.getElementById('item_discription').innerHTML = "";
          listnumber = 0;
          checkout_button.removeAttribute("class", "checkout_ready");
          checkout_button.innerHTML = "CHECK OUT";
          checkout_button.removeEventListener("onclick", Checkout);
          listitems = [];
        };

        function Checkout() {
            store_id = document.getElementById("store_id").innerHTML;
            register_number = document.getElementById("register_id").innerHTML;
            reciept = document.getElementById("item_total_sec").innerHTML;
            reciept_total = document.getElementById("total").innerHTML;
            fetch('/checkout/', {
              method: 'POST',
              body: JSON.stringify({ store : store_id, register : register_number, items : listitems, reciept :reciept, total:reciept_total})
              })
            .then(response => response.json())
            .then(data => {
              if (data.status == "Successful") {
                VoidReg()
              } else {
                console.log("EORROR")
              } })
        };


      function Lookup(upc) {
        fetch('/lookup/', {
          method: 'POST',
          body: JSON.stringify({ upc : upc})
          })
        .then(response => response.json())
        .then(data => {
          listitems.push(data.upc);
          item_model = document.getElementById('item_model').cloneNode();
          item_model.name = "bill_item";
          item_model.id = "item/"+listnumber;
          item_model.innerHTML = "<div name='count' class='item_tag' style='width: 6%;'>"+listnumber+"</div><div class='item_tag' style='width: 34%;'>"+data.name+"</div><div class='item_tag' name='item_price' style='width: 11.33%;'>"+data.price+"</div><div class='item_tag' name='item_tax' style='width: 11.33%;'>"+data.tax+"</div><div id='qty/"+listnumber+"'class='item_tag'>1</div>x";
          document.getElementById('item_bill_sec').appendChild(item_model);
          makeSelectable(item_model);
          document.getElementById('item_discription').innerHTML = data.discription;
          listnumber++;
          add_price(parseFloat(data.price), parseFloat(data.tax), 1);
          var element = document.getElementById("checkout_button");
          if (document.getElementsByClassName('checkout_ready')[0] === null) {
            return
          }
          else {
            checkout_button.onclick =  Checkout;
            checkout_button.setAttribute("class", "checkout_ready");
          }
        }) }



      const upc_input = document.getElementById('upc_input');
      upc_input.addEventListener("keyup", function(event) {
        // Number 13 is the "Enter" key on the keyboard
        if (event.keyCode === 13) {
          // Cancel the default action, if needed
          event.preventDefault();
          new_lookup = upc_input.value;
          Lookup(new_lookup);
        }
      });
      document.getElementById('void_button').onclick = VoidReg;

      document.getElementById('adj_button').addEventListener("click" , function () {
        if (document.getElementsByClassName("selected")[0] === null) {
          return
        }
        else {
          let selected = document.getElementsByClassName("selected")[0];
          document.getElementById("number_amount").style.display = "block";
          document.getElementById('amount').addEventListener("keyup", function update_qty() {
            if (event.keyCode === 13) {
            document.getElementById("number_amount").style.display = "none";
            newval = parseFloat(document.getElementById("amount").value);
            tax = parseFloat(selected.childNodes[2].childNodes[1].innerHTML);
            price = parseFloat(selected.childNodes[2].childNodes[0].innerHTML);
            old_qty = parseFloat(selected.childNodes[2].childNodes[2].innerHTML);
            selected.childNodes[2].childNodes[2].innerHTML = newval;
            sub_price(price, tax, old_qty);
            add_price(price, tax, newval);
            document.getElementById("amount").value = 1;
            document.getElementById('amount').removeEventListener("keyup", update_qty);
          } })
        } })

        document.getElementById("del_button").onclick = function() {
          let selected = document.getElementsByClassName("selected")[0];
          if (selected === null) {
            return
          } else {
            tax = parseFloat(selected.childNodes[2].childNodes[1].innerHTML);
            price = parseFloat(selected.childNodes[2].childNodes[0].innerHTML);
            old_qty = parseFloat(selected.childNodes[2].childNodes[2].innerHTML);
            sub_price(price, tax, old_qty);
            function reorder() {
              list = document.getElementsByName("count");
              for (var i = 0; i < list.length; i++) {
                list[i].innerHTML = i;
                listnumber = i;
              } }
            selected.remove();
            reorder();
          } };

        document.getElementById("disc_button").onclick = function () {
          if (document.getElementsByClassName("selected")[0] === null) {
            return
          } else {
            let selected = document.getElementsByClassName("selected")[0];
            document.getElementById("number_amount").style.display = "block";
            document.getElementById('amount').addEventListener("keyup", function update_qty() {
              if (event.keyCode === 13) {
              document.getElementById("number_amount").style.display = "none";
              discount = parseFloat(document.getElementById("amount").value) * 0.01;
              discount_rate = 1 - discount;
              price = parseFloat(selected.childNodes[2].childNodes[0].innerHTML);
              qty = parseFloat(selected.childNodes[2].childNodes[2].innerHTML);
              tax = parseFloat(selected.childNodes[2].childNodes[1].innerHTML);
              new_price = discount_rate * price;
              sub_price(price, tax, qty);
              add_price(new_price, tax, qty);
              selected.childNodes[2].childNodes[0].innerHTML = new_price.toFixed(2)
              discdiv = document.createElement("div")
              discdiv.innerHTML = "Disc%"+parseFloat(document.getElementById("amount").value);
              discdiv.style.float = "right"
              if (selected.childNodes.length == 4) {
                selected.childNodes[3].remove();
              }
              selected.childNodes[2].insertAdjacentElement("afterend", discdiv)
              document.getElementById("amount").value = 1;
              document.getElementById('amount').removeEventListener("keyup", update_qty);
            } })
          }};

          document.getElementById("item_lookup_input").addEventListener("keyup", function () {
            let name = this.value;
            fetch('/lookup_name/', {
              method: 'POST',
              body: JSON.stringify({ name : name})
            }).then(response => response.json())
            .then(data => {
              lookup_sec = document.getElementById("results_sec");
              lookup_sec.innerHTML = "<table id='lookup_table'><tr><th>BARCODE</th><th>NAME</th><th>PRICE</th><th>TAX</th><th>QTY</th></tr></table>";
              lookup_table = document.getElementById("lookup_table").childNodes[0];
              for (var i = 0; i < data.length; i++) {
                list_item = document.createElement("tr");
                list_item.innerHTML = "<td>"+data[i].fields.barcode+"</td><td>"+data[i].fields.title+"</td><td>"+data[i].fields.price+"</td><td>"+data[i].fields.tax+"</td>"+"<td>1</td>";
                makeSelectable(list_item, data[i].fields.barcode);
                lookup_table.append(list_item);
              }
            })
          })

            document.getElementById('item_lookup_button').onclick = function () {
            document.getElementById('item_lookup_sec').style.display = "block";
            document.getElementById("lookup_t_x").onclick = function () {
            document.getElementById('item_lookup_sec').style.display = "none";
            document.getElementById('results_sec').innerHTML = "";
          }}


          document.getElementById('transaction_lookup_button').onclick = function () {
            document.getElementById('reciept_lookup_sec').style.display = "block";
            document.getElementById("lookup_x").onclick = function () {
            document.getElementById('reciept_lookup_sec').style.display = "none";
            document.getElementById('t_results_sec').innerHTML = "";
          }}
          document.getElementById("rec_lookup_input").addEventListener("keyup", function () {
            let name = this.value;
            fetch('/reciept_lookup/', {
              method: 'POST',
              body: JSON.stringify({ reciept : name})
            }).then(response => response.json())
            .then(data => {
              console.log(data);
              document.getElementById('t_results_sec').innerHTML = data.reciept;
            })
          })



    }
})
