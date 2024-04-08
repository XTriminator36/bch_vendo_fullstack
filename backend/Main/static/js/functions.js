$(function() {
    // Hide offline message
    $("#offline").hide();

    // Initialize global variables
    var curTxHash;
    var prevTxHash;
    var totalPayable;
    var bchToPHPRate;
    var rotation;
    var channel;
    var bchAddress;
    var paid = false;

    var a01Qty = "{{a01.quantity}}";
    var a02Qty = "{{a02.quantity}}";
    var a03Qty = "{{a03.quantity}}";
    var a04Qty = "{{a04.quantity}}";
    var b05Qty = "{{b05.quantity}}";
    var b06Qty = "{{b06.quantity}}";
    var b07Qty = "{{b07.quantity}}";
    var b08Qty = "{{b08.quantity}}";
    var c09Qty = "{{c09.quantity}}";
    var c10Qty = "{{c10.quantity}}";
    var c11Qty = "{{c11.quantity}}";
    var c12Qty = "{{c12.quantity}}";
    var d13Qty = "{{d13.quantity}}";
    var d14Qty = "{{d14.quantity}}";
    var d15Qty = "{{d15.quantity}}";
    var d16Qty = "{{d16.quantity}}";

    var a01QtyStockTxt = "Stock:" + " " + a01Qty;
    var a02QtyStockTxt = "Stock:" + " " + a02Qty;
    var a03QtyStockTxt = "Stock:" + " " + a03Qty;
    var a04QtyStockTxt = "Stock:" + " " + a04Qty;
    var b05QtyStockTxt = "Stock:" + " " + b05Qty;
    var b06QtyStockTxt = "Stock:" + " " + b06Qty;
    var b07QtyStockTxt = "Stock:" + " " + b07Qty;
    var b08QtyStockTxt = "Stock:" + " " + b08Qty;
    var c09QtyStockTxt = "Stock:" + " " + c09Qty;
    var c10QtyStockTxt = "Stock:" + " " + c10Qty;
    var c11QtyStockTxt = "Stock:" + " " + c11Qty;
    var c12QtyStockTxt = "Stock:" + " " + c12Qty;
    var d13QtyStockTxt = "Stock:" + " " + d13Qty;
    var d14QtyStockTxt = "Stock:" + " " + d14Qty;
    var d15QtyStockTxt = "Stock:" + " " + d15Qty;
    var d16QtyStockTxt = "Stock:" + " " + d16Qty;

    $("#a01-quantity").text(a01QtyStockTxt);
    $("#a02-quantity").text(a02QtyStockTxt);
    $("#a03-quantity").text(a03QtyStockTxt);
    $("#a04-quantity").text(a04QtyStockTxt);
    $("#b05-quantity").text(b05QtyStockTxt);
    $("#b06-quantity").text(b06QtyStockTxt);
    $("#b07-quantity").text(b07QtyStockTxt);
    $("#b08-quantity").text(b08QtyStockTxt);
    $("#c09-quantity").text(c09QtyStockTxt);
    $("#c10-quantity").text(c10QtyStockTxt);
    $("#c11-quantity").text(c11QtyStockTxt);
    $("#c12-quantity").text(c12QtyStockTxt);
    $("#d13-quantity").text(d13QtyStockTxt);
    $("#d14-quantity").text(d14QtyStockTxt);
    $("#d15-quantity").text(d15QtyStockTxt);
    $("#d16-quantity").text(d16QtyStockTxt);

    $("#a01-qty-modal").text(a01QtyStockTxt);
    $("#a02-qty-modal").text(a02QtyStockTxt);
    $("#a03-qty-modal").text(a03QtyStockTxt);
    $("#a04-qty-modal").text(a04QtyStockTxt);
    $("#b05-qty-modal").text(b05QtyStockTxt);
    $("#b06-qty-modal").text(b06QtyStockTxt);
    $("#b07-qty-modal").text(b07QtyStockTxt);
    $("#b08-qty-modal").text(b08QtyStockTxt);
    $("#c09-qty-modal").text(c09QtyStockTxt);
    $("#c10-qty-modal").text(c10QtyStockTxt);
    $("#c11-qty-modal").text(c11QtyStockTxt);
    $("#c12-qty-modal").text(c12QtyStockTxt);
    $("#d13-qty-modal").text(d13QtyStockTxt);
    $("#d14-qty-modal").text(d14QtyStockTxt);
    $("#d15-qty-modal").text(d15QtyStockTxt);
    $("#d16-qty-modal").text(d16QtyStockTxt);

    // Call checkQuantity
    checkQuantity();

    // Call ajaxCall function every 3 seconds to check new transactions
    setInterval(ajaxCall, 3000);

    // Get current BCH to PHP rate 
    $.get("https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=PHP",function(data){
        bchToPHPRate = data["PHP"]
    });


    // Function for showing QR code modal after clicking on purchase button
    // Also for displaying total payable and setting the payable
    $(
        "#a01-purchase-btn, #a02-purchase-btn, #a03-purchase-btn, #a04-purchase-btn, #b05-purchase-btn, #b06-purchase-btn, #b07-purchase-btn, #b08-purchase-btn, #c09-purchase-btn, #c10-purchase-btn, #c11-purchase-btn, #c12-purchase-btn, #d13-purchase-btn, #d14-purchase-btn, #d15-purchase-btn, #d16-purchase-btn"
    ).click(function(){
        $('#qrcodeModal').modal('show');
        $('#qrcode').kjua({text: bchAddress + '?amount=' + totalPayable, size: 400,});
        // setTimeout(function(){$('#qrcodeModal').modal('hide')},300000);
        $("#payable").text('BCH ' + totalPayable);

        console.log('Channel: ', channel)
    });

    $('#qrcodeModal').on('hidden.bs.modal', function (e) {
        $('#qrcode').empty()
    })


    // Function checking product available quantity
    function checkQuantity() {
        if (parseInt(a01Qty) == 0) {
            $("#a01-quantity").attr('class', 'badge badge-danger');
            $("#card-1").attr("data-target", "outOfStockModal");
            $("#card-1").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                $(".outOfStockModal").css("background", "#333333ab");
                return false;
            });
        } else {
            $("#a01-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(a02Qty) == 0) {
            $("#a02-quantity").attr('class', 'badge badge-danger');
            $("#card-2").attr("data-target", "outOfStockModal");
            $("#card-2").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                $(".outOfStockModal").css("background", "#333333ab");
                return false;
            });

        } else {
            $("#a02-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(a03Qty) == 0) {
            $("#a03-quantity").attr('class', 'badge badge-danger');
            $("#card-3").attr("data-target", "outOfStockModal");
            $("#card-3").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                $(".outOfStockModal").css("background", "#333333ab");
                return false;
            });
        } else {
            $("#a03-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(a04Qty) == 0) {
            $("#a04-quantity").attr('class', 'badge badge-danger');
            $("#card-4").attr("data-target", "outOfStockModal");
            $("#card-4").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                $(".outOfStockModal").css("background", "#333333ab");
                return false;
            });
        } else {
            $("#a04-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(b05Qty) == 0) {
            $("#b05-quantity").attr('class', 'badge badge-danger');
            $("#card-5").attr("data-target", "outOfStockModal");
            $("#card-5").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
            });
        } else {
            $("#b05-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(b06Qty) == 0) {
            $("#b06-quantity").attr('class', 'badge badge-danger');
            $("#card-6").attr("data-target", "outOfStockModal");
            $("#card-6").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
            });
        } else {
            $("#b06-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(b07Qty) == 0) {
            $("#b07-quantity").attr('class', 'badge badge-danger');
            $("#card-7").attr("data-target", "outOfStockModal");
            $("#card-7").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
            });
        } else {
            $("#b07-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(b08Qty) == 0) {
            $("#b08-quantity").attr('class', 'badge badge-danger');
            $("#card-8").attr("data-target", "outOfStockModal");
            $("#card-8").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
            });
        } else {
            $("#b08-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(c09Qty) == 0) {
            $("#c09-quantity").attr('class', 'badge badge-danger');
            $("#card-9").attr("data-target", "outOfStockModal");
            $("#card-9").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
            });
        } else {
            $("#c09-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(c10Qty) == 0) {
            $("#c10-quantity").attr('class', 'badge badge-danger');
            $("#card-10").attr("data-target", "outOfStockModal");
            $("#card-10").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
            });
        } else {
            $("#c10-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(c11Qty) == 0) {
            $("#c11-quantity").attr('class', 'badge badge-danger');
            $("#card-11").attr("data-target", "outOfStockModal");
            $("#card-11").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
            });
        } else {
            $("#c11-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(c12Qty) == 0) {
            $("#c12-quantity").attr('class', 'badge badge-danger');
            $("#card-12").attr("data-target", "outOfStockModal");
            $("#card-12").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
            });
        } else {
            $("#c12-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(d13Qty) == 0) {
            $("#d13-quantity").attr('class', 'badge badge-danger');
            $("#card-13").attr("data-target", "outOfStockModal");
            $("#card-13").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
            });
        } else {
            $("#d13-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(d14Qty) == 0) {
            $("#d14-quantity").attr('class', 'badge badge-danger');
            $("#card-14").attr("data-target", "outOfStockModal");
            $("#card-14").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
            });
        } else {
            $("#d14-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(d15Qty) == 0) {
            $("#d15-quantity").attr('class', 'badge badge-danger');
            $("#card-15").attr("data-target", "outOfStockModal");
            $("#card-15").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
            });
        } else {
            $("#d15-quantity").attr('class', 'badge badge-success');
        };

        if (parseInt(d16Qty) == 0) {
            $("#d16-quantity").attr('class', 'badge badge-danger');
            $("#card-16").attr("data-target", "outOfStockModal");
            $("#card-16").click(function(){
                $("#outOfStockModal").modal('show');
                setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
            });
        } else {
            $("#d16-quantity").attr('class', 'badge badge-success');
        };

    };


    // Notification function using Toastr library
    function paymentNotification(){
        toastr.options.timeOut = 3000;
        toastr.options.positionClass = 'toast-bottom-center';
        toastr.success("Amount " + payment, 'Payment received!');
    }


    // Function listening for BCH transaction
    function ajaxCall() {
        prevTxHash = curTxHash

        // Get current BCH to PHP rate 
        $.get("https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=PHP",function(data){
            bchToPHPRate = data["PHP"]
        });
        
        $.ajax({ 
            type:"GET", 
            url: "check-tx-hash", 
            success: function( data ) 
            { 
                curTxHash = data.hash;
                offline = data.offline ;
                
                bchAddress = data.bchAddress;
                $("#bch-address").text(bchAddress);

                // $("#fiat").text('BCH ' + parseFloat(payableBalance.toFixed(10)));

                $("#balance-payable").hide()
                $("#balance-payable-fiat").hide()

                console.log("Total Payable: ", price);
                console.log(data)

                // Display fiat on price of each product on the list
                $("#a01-price-fiat").text("~ " + "PHP " + (parseFloat("{{a01.price}}") * bchToPHPRate).toFixed(2));
                $("#a02-price-fiat").text("~ " + "PHP " + (parseFloat("{{a02.price}}") * bchToPHPRate).toFixed(2));
                $("#a03-price-fiat").text("~ " + "PHP " + (parseFloat("{{a03.price}}") * bchToPHPRate).toFixed(2));
                $("#a04-price-fiat").text("~ " + "PHP " + (parseFloat("{{a04.price}}") * bchToPHPRate).toFixed(2));
                $("#b05-price-fiat").text("~ " + "PHP " + (parseFloat("{{b05.price}}") * bchToPHPRate).toFixed(2));
                $("#b06-price-fiat").text("~ " + "PHP " + (parseFloat("{{b06.price}}") * bchToPHPRate).toFixed(2));
                $("#b07-price-fiat").text("~ " + "PHP " + (parseFloat("{{b07.price}}") * bchToPHPRate).toFixed(2));
                $("#b08-price-fiat").text("~ " + "PHP " + (parseFloat("{{b08.price}}") * bchToPHPRate).toFixed(2));
                $("#c09-price-fiat").text("~ " + "PHP " + (parseFloat("{{c09.price}}") * bchToPHPRate).toFixed(2));
                $("#c10-price-fiat").text("~ " + "PHP " + (parseFloat("{{c10.price}}") * bchToPHPRate).toFixed(2));
                $("#c11-price-fiat").text("~ " + "PHP " + (parseFloat("{{c11.price}}") * bchToPHPRate).toFixed(2));
                $("#c12-price-fiat").text("~ " + "PHP " + (parseFloat("{{c12.price}}") * bchToPHPRate).toFixed(2));
                $("#d13-price-fiat").text("~ " + "PHP " + (parseFloat("{{d13.price}}") * bchToPHPRate).toFixed(2));
                $("#d14-price-fiat").text("~ " + "PHP " + (parseFloat("{{d14.price}}") * bchToPHPRate).toFixed(2));
                $("#d15-price-fiat").text("~ " + "PHP " + (parseFloat("{{d15.price}}") * bchToPHPRate).toFixed(2));
                $("#d16-price-fiat").text("~ " + "PHP " + (parseFloat("{{d16.price}}") * bchToPHPRate).toFixed(2));

                //remove comment if deployment

                // if (offline) {
                //     $("#main").hide();
                //     $("#offline").show();
                // }

                console.log("Payload for update-quantity request:")
                console.log("section: ", channel)
                console.log("txHash: ", curTxHash)

                console.log('Compare hashes:', prevTxHash, curTxHash)
                if (prevTxHash && prevTxHash != curTxHash) {
                    if (typeof(curTxHash)  != "undefined" && curTxHash.length == 64){
                        paid = false
                        console.log("Transaction detected!!")

                        // Hide QRcode after successful transaction
                        $('#qrcodeModal').modal('hide');

                        // Show success modal and hide automatically after 10 seconds
                        if (paid == false) {
                            $('#successModal').modal('show');
                            setTimeout(function(){$('#successModal').modal('hide')},10000);
                        }

                        // Update stock quantity in database
                        $.ajax({
                            type: "POST",
                            url: "update-quantity/",
                            headers: { "X-CSRFToken": '{{csrf_token}}' },
                            data: {
                                'section': channel,
                                'txHash': curTxHash
                            },
                            success: function (msg) {
                                success = msg["success"]
                                if (success) {
                                    paid = true
                                    console.log("Triggering to dispense...")
                                    console.log("Channel: ", channel)
                                }

                                if (msg['section'] == '1') {
                                    console.log(msg)
                                    a01Qty = msg['balanceQuantity']
                                    $("#a01-quantity").text("Stock:" + " " + a01Qty);
                                    $("#a01-qty-modal").text("Stock:" + " " + a01Qty);
                                    if (parseInt(a01Qty) == 0) {
                                        $("#a01-quantity").attr('class', 'badge badge-danger');
                                        $("#card-1").attr("data-target", "outOfStockModal");
                                        $("#card-1").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '2') {
                                    a02Qty = msg['balanceQuantity']
                                    $("#a02-quantity").text("Stock:" + " " + a02Qty);
                                    $("#a02-qty-modal").text("Stock:" + " " + a02Qty);
                                    if (parseInt(a02Qty) == 0) {
                                        $("#a02-quantity").attr('class', 'badge badge-danger');
                                        $("#card-2").attr("data-target", "outOfStockModal");
                                        $("#card-2").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '3') {
                                    a03Qty = msg['balanceQuantity']
                                    $("#a03-quantity").text("Stock:" + " " + a03Qty);
                                    $("#a03-qty-modal").text("Stock:" + " " + a03Qty);
                                    if (parseInt(a03Qty) == 0) {
                                        $("#a03-quantity").attr('class', 'badge badge-danger');
                                        $("#card-3").attr("data-target", "outOfStockModal");
                                        $("#card-3").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '4') {
                                    a04Qty = msg['balanceQuantity']
                                    $("#a04-quantity").text("Stock:" + " " + a04Qty);
                                    $("#a04-qty-modal").text("Stock:" + " " + a04Qty);
                                    if (parseInt(a04Qty) == 0) {
                                        $("#a04-quantity").attr('class', 'badge badge-danger');
                                        $("#card-4").attr("data-target", "outOfStockModal");
                                        $("#card-4").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '5') {
                                    b05Qty = msg['balanceQuantity']
                                    $("#b05-quantity").text("Stock:" + " " + b05Qty);
                                    $("#b05-qty-modal").text("Stock:" + " " + b05Qty);
                                    if (parseInt(b05Qty) == 0) {
                                        $("#b05-quantity").attr('class', 'badge badge-danger');
                                        $("#card-5").attr("data-target", "outOfStockModal");
                                        $("#card-5").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '6') {
                                    b06Qty = msg['balanceQuantity']
                                    $("#b06-quantity").text("Stock:" + " " + b06Qty);
                                    $("#b06-qty-modal").text("Stock:" + " " + b06Qty);
                                    if (parseInt(b06Qty) == 0) {
                                        $("#b06-quantity").attr('class', 'badge badge-danger');
                                        $("#card-6").attr("data-target", "outOfStockModal");
                                        $("#card-6").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '7') {
                                    b07Qty = msg['balanceQuantity']
                                    $("#b07-quantity").text("Stock:" + " " + b07Qty);
                                    $("#b07-qty-modal").text("Stock:" + " " + b07Qty);
                                    if (parseInt(b07Qty) == 0) {
                                        $("#b07-quantity").attr('class', 'badge badge-danger');
                                        $("#card-7").attr("data-target", "outOfStockModal");
                                        $("#card-7").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '8') {
                                    b08Qty = msg['balanceQuantity']
                                    $("#b08-quantity").text("Stock:" + " " + b08Qty);
                                    $("#b08-qty-modal").text("Stock:" + " " + b08Qty);
                                    if (parseInt(b08Qty) == 0) {
                                        $("#b08-quantity").attr('class', 'badge badge-danger');
                                        $("#card-8").attr("data-target", "outOfStockModal");
                                        $("#card-8").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '9') {
                                    c09Qty = msg['balanceQuantity']
                                    $("#c09-quantity").text("Stock:" + " " + c09Qty);
                                    $("#c09-qty-modal").text("Stock:" + " " + c09Qty);
                                    if (parseInt(c09Qty) == 0) {
                                        $("#c09-quantity").attr('class', 'badge badge-danger');
                                        $("#card-9").attr("data-target", "outOfStockModal");
                                        $("#card-9").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '10') {
                                    c10Qty = msg['balanceQuantity']
                                    $("#c10-quantity").text("Stock:" + " " + c10Qty);
                                    $("#c10-qty-modal").text("Stock:" + " " + c10Qty);
                                    if (parseInt(c10Qty) == 0) {
                                        $("#c10-quantity").attr('class', 'badge badge-danger');
                                        $("#card-10").attr("data-target", "outOfStockModal");
                                        $("#card-10").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '11') {
                                    c11Qty = msg['balanceQuantity']
                                    $("#c11-quantity").text("Stock:" + " " + c11Qty);
                                    $("#c11-qty-modal").text("Stock:" + " " + c11Qty);
                                    if (parseInt(c11Qty) == 0) {
                                        $("#c11-quantity").attr('class', 'badge badge-danger');
                                        $("#card-11").attr("data-target", "outOfStockModal");
                                        $("#card11").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '12') {
                                    c12Qty = msg['balanceQuantity']
                                    $("#c12-quantity").text("Stock:" + " " + c12Qty);
                                    $("#c12-qty-modal").text("Stock:" + " " + c12Qty);
                                    if (parseInt(c12Qty) == 0) {
                                        $("#c12-quantity").attr('class', 'badge badge-danger');
                                        $("#card-12").attr("data-target", "outOfStockModal");
                                        $("#card-12").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '13') {
                                    d13Qty = msg['balanceQuantity']
                                    $("#d13-quantity").text("Stock:" + " " + d13Qty);
                                    $("#d13-qty-modal").text("Stock:" + " " + d13Qty);
                                    if (parseInt(d13Qty) == 0) {
                                        $("#d13-quantity").attr('class', 'badge badge-danger');
                                        $("#card-13").attr("data-target", "outOfStockModal");
                                        $("#card-13").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '14') {
                                    d14Qty = msg['balanceQuantity']
                                    $("#d14-quantity").text("Stock:" + " " + d14Qty);
                                    $("#d14-qty-modal").text("Stock:" + " " + d14Qty);
                                    if (parseInt(d14Qty) == 0) {
                                        $("#d14-quantity").attr('class', 'badge badge-danger');
                                        $("#card-14").attr("data-target", "outOfStockModal");
                                        $("#card-14").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '15') {
                                    d15Qty = msg['balanceQuantity']
                                    $("#d15-quantity").text("Stock:" + " " + d15Qty);
                                    $("#d15-qty-modal").text("Stock:" + " " + d15Qty);
                                    if (parseInt(d15Qty) == 0) {
                                        $("#d15-quantity").attr('class', 'badge badge-danger');
                                        $("#card-15").attr("data-target", "outOfStockModal");
                                        $("#card-15").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                } else if (msg['section'] == '16') {
                                    d16Qty = msg['balanceQuantity']
                                    $("#d16-quantity").text("Stock:" + " " + d16Qty);
                                    $("#d16-qty-modal").text("Stock:" + " " + d16Qty);
                                    if (parseInt(d16Qty) == 0) {
                                        $("#d16-quantity").attr('class', 'badge badge-danger');
                                        $("#card-16").attr("data-target", "outOfStockModal");
                                        $("#card-16").click(function(){
                                            $("#outOfStockModal").modal('show');
                                            setTimeout(function(){$('#outOfStockModal').modal('hide')},3000);
                                            $(".outOfStockModal").css("background", "#333333ab");
                                            return false;
                                        });
                                    }
                                }

                            }
                        });
                    }
                }       
            }, 

            // Show/hide loading image during initial opening 

            // remove comment when deployment

            // complete: function(){
            //     $('#loading').hide();
            //     if (offline) {
            //         $("#main").hide();
            //         $("#offline").show();
            //     } else {
            //         $("#main").show();
            //         $("#offline").hide();  
            //     }
            // }

        })
    }


    // QR code modal fiat price display
    $('#qrcodeModal').on('shown.bs.modal', function () {
        $("#payable-fiat").text("~ " + "PHP " + (totalPayable * bchToPHPRate).toFixed(2));
    });


    // TODO: Create a function to reduce redundunt codes
    // Capture event on each modal when user selects a product			
    // A01
    $('#a01-Modal').on('shown.bs.modal', function () {
        var a01Price = parseFloat("{{a01.price}}")

        channel = 0
        console.log('Channel: ', channel)

        totalPayable = a01Price
        $("#a01-Modal #total-price-display").val(totalPayable)

        $("#a01-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{a01.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // A02
    $('#a02-Modal').on('shown.bs.modal', function () {
        var a02Price = parseFloat("{{a02.price}}")

        channel = 1
        console.log('Channel: ', channel)

        totalPayable = a02Price
        $("#a02-Modal #total-price-display").val(totalPayable)

        $("#a02-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{a02.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // A03
    $('#a03-Modal').on('shown.bs.modal', function () {
        var a03Price = parseFloat("{{a03.price}}")

        channel = 2
        console.log('Channel: ', channel)

        totalPayable = a03Price
        $("#a03-Modal #total-price-display").val(totalPayable)

        $("#a03-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{a03.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // A04
    $('#a04-Modal').on('shown.bs.modal', function () {
        var a04Price = parseFloat("{{a04.price}}")

        channel = 3
        console.log('Channel: ', channel)

        totalPayable = a04Price
        $("#a04-Modal #total-price-display").val(totalPayable)

        $("#a04-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{a04.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // B05
    $('#b05-Modal').on('shown.bs.modal', function () {
        var b05Price = parseFloat("{{b05.price}}")

        channel = 4
        console.log('Channel: ', channel)

        totalPayable = b05Price
        $("#b05-Modal #total-price-display").val(totalPayable)

        $("#b05-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{b05.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // B06
    $('#b06-Modal').on('shown.bs.modal', function () {
        var b06Price = parseFloat("{{b06.price}}")

        channel = 5
        console.log('Channel: ', channel)

        totalPayable = b06Price
        $("#b06-Modal #total-price-display").val(totalPayable)

        $("#b06-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{b06.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // B07
    $('#b07-Modal').on('shown.bs.modal', function () {
        var b07Price = parseFloat("{{b07.price}}")

        channel = 6
        console.log('Channel: ', channel)

        totalPayable = b07Price
        $("#b07-Modal #total-price-display").val(totalPayable)

        $("#b07-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{b07.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // B08
    $('#b08-Modal').on('shown.bs.modal', function () {
        var b08Price = parseFloat("{{b08.price}}")

        channel = 7
        console.log('Channel: ', channel)

        totalPayable = b08Price
        $("#b08-Modal #total-price-display").val(totalPayable)

        $("#b08-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{b08.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // C09
    $('#c09-Modal').on('shown.bs.modal', function () {
        var c09Price = parseFloat("{{c09.price}}")

        channel = 8
        console.log('Channel: ', channel)

        totalPayable = c09Price * c09SelectedQuantity
        $("#c09-Modal #total-price-display").val(totalPayable)

        $("#c09-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{c09.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // C10
    $('#c10-Modal').on('shown.bs.modal', function () {
        var c10Price = parseFloat("{{c10.price}}")

        channel = 9
        console.log('Channel: ', channel)

        totalPayable = c10Price * c10SelectedQuantity
        $("#c10-Modal #total-price-display").val(totalPayable)

        $("#c10-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{c10.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // C11
    $('#c11-Modal').on('shown.bs.modal', function () {
        var c11Price = parseFloat("{{c11.price}}")

        channel = 10
        console.log('Channel: ', channel)

        totalPayable = c11Price
        $("#c11-Modal #total-price-display").val(totalPayable)

        $("#c11-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{c11.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // C12
    $('#c12-Modal').on('shown.bs.modal', function () {
        var c12Price = parseFloat("{{c12.price}}")

        channel = 11
        console.log('Channel: ', channel)

        totalPayable = c12Price
        $("#c12-Modal #total-price-display").val(totalPayable)

        $("#c12-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{c12.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // D13
    $('#d13-Modal').on('shown.bs.modal', function () {
        var d13Price = parseFloat("{{d13.price}}")

        channel = 12
        console.log('Channel: ', channel)

        totalPayable = d13Price
        $("#d13-Modal #total-price-display").val(totalPayable)

        $("#d13-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{d13.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // D14
    $('#d14-Modal').on('shown.bs.modal', function () {
        var d14Price = parseFloat("{{d14.price}}")

        channel = 13
        console.log('Channel: ', channel)

        totalPayable = d14Price
        $("#d14-Modal #total-price-display").val(totalPayable)

        $("#d14-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{d14.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });       

    // D15
    $('#d15-Modal').on('shown.bs.modal', function () {
        var d15Price = parseFloat("{{d15.price}}")

        channel = 14
        console.log('Channel: ', channel)

        totalPayable = d15Price
        $("#d15-Modal #total-price-display").val(totalPayable)

        $("#d15-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{d15.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

    // D16
    $('#d16-Modal').on('shown.bs.modal', function () {
        var d16Price = parseFloat("{{d16.price}}")

        channel = 15
        console.log('Channel: ', channel)

        totalPayable = d16Price
        $("#d16-Modal #total-price-display").val(totalPayable)

        $("#d16-price-fiat-modal").text("~ " + "PHP " + (parseFloat("{{d16.price}}") * bchToPHPRate).toFixed(2));

        checkQuantity();
    });

});
