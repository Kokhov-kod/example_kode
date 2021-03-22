


    	<?php
					
					mb_internal_encoding("UTF-8");
					$data = $_POST;

					 $link=mysqli_connect('podd550897.mysql', 'podd550897_poddo', 'PodDone2021', 'podd550897_poddone')
						or die("Ошибка " . mysqli_error($link)); 
					
					$url = ((!empty($_SERVER['HTTPS'])) ? 'https' : 'http') . '://' . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];
					
					$n = $_GET['id'];

 				    
					$query ="SELECT * FROM `products` WHERE id='$n'";

					$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
					while($row = mysqli_fetch_array($result)){


					    	$id=$row['id'];
					    	$name=$row['name'];
					    	$price=$row['price'];
					    	$description=$row['description'];
					 		$img=$row['image'];
					 		
					 		$name = iconv( 'cp1251', 'utf8', $name );
					 		$description = iconv( 'cp1251', 'utf8', $description );

				    }
				    
					  
					?>
 
<!DOCTYPE html>
<html><head>
    <!-- Yandex.Metrika counter -->
<script type="text/javascript" >
   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

   ym(72188359, "init", {
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true,
        webvisor:true,
        ecommerce:"dataLayer"
   });
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/72188359" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->
    <!-- Yandex.Metrika counter -->
<script type="text/javascript" >
   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

   ym(71919988, "init", {
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true,
        webvisor:true,
        ecommerce:"dataLayer"
   });
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/71919988" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->
    <title>PodDone</title>
    
<style>
    /* слой затемнения */
.dm-overlay {
    position: fixed;
    top: 0;
    left: 0;
    background: rgba(0, 0, 0, 0.65);
    display: none;
    overflow: auto;
    width: 100%;
    height: 100%;
    z-index: 1000;
}
/* активируем слой затемнения и модальное окно */
.dm-overlay:target {
    display: block;
/* анимация и время задержки */
    -webkit-animation: fade .6s;
    -moz-animation: fade .6s;
    animation: fade .6s;
}
/* блочная таблица */
.dm-table {
    display: table;
    width: 100%;
    height: 100%;
}
/* ячейка блочной таблицы */
.dm-cell {
    display: table-cell;
    padding: 0 1em;
    vertical-align: middle;
    text-align: center;
}
/* модальный блок */
.dm-modal {
    display: inline-block;
    padding: 20px;
/* максимально возможная ширина */
    max-width: 50em;
    background: #607d8b;
/* внешняя тень блока */
    -webkit-box-shadow: 0px 15px 20px rgba(0, 0, 0, 0.22), 0px 19px 60px rgba(0, 0, 0, 0.3);
    -moz-box-shadow: 0px 15px 20px rgba(0, 0, 0, 0.22), 0px 19px 60px rgba(0, 0, 0, 0.3);
    box-shadow: 0px 15px 20px rgba(0, 0, 0, 0.22), 0px 19px 60px rgba(0, 0, 0, 0.3);
    color: #fff;
    text-align: left;
/* анимация и время задержки */
    -webkit-animation: fade .8s;
    -moz-animation: fade .8s;
    animation: fade .8s;
}
</style>
<style>
    *, *:after, *:before { 
   -webkit-box-sizing: border-box;
   -moz-box-sizing: border-box;
   box-sizing: border-box; 
}
 
/* базовый стиль формы */
form {
    overflow: hidden;
    margin: 0 auto;
    padding: 30px 30px 6px 30px;
    min-width: 320px;
    max-width: 520px;
    width: 100%;
    border: 1px solid rgba(120,120,120,.7);
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
    background: rgba(60, 63, 65, 0.9); 
    -webkit-background-clip: padding-box;
    -moz-background-clip: padding;
    background-clip: padding-box;
    -webkit-box-shadow: 0 0 13px 3px rgba(0,0,0,.5);
    -moz-box-shadow: 0 0 13px 3px rgba(0,0,0,.5);
    box-shadow: 0 0 13px 3px rgba(0,0,0,.5);
}
/*общие стили полей ввода*/
textarea, input{
    display:block;    
    margin-bottom:20px;
    padding-right:20px;
    padding-left:20px;
    -webkit-border-radius: 4px;
    -moz-border-radius: 4px;
    border-radius: 4px;
    -webkit-background-clip: padding-box;
    -moz-background-clip: padding;
    background-clip: padding-box; 
    color:#fff;
    font-weight: 300;
    font-size:18px;
    font-family: 'Open Sans', sans-serif;
}
/* поле сообщения */
textarea{
    overflow:hidden;
    width: 100%;
    height: 110px;
    border: 1px solid rgba(255,255,255,.6);
    background: rgba(255, 255, 255, 0.4); 
}
/* поля ввода */
input {
    width: 100%;
    height: 48px;
    border: 1px solid rgba(255,255,255,.4);
}
input[type=submit] {
    cursor:pointer;
}
input.name {
   background: rgba(255, 255, 255, 0.4); 
   padding-left:25px;
}
input.email {
   background: rgba(255, 255, 255, 0.4);
   padding-left:25px;
}
input.message {
   background: rgba(255, 255, 255, 0.4);
   padding-left:25px;
}
::-webkit-input-placeholder {
   color: #fff;
}
:-moz-placeholder{ 
   color: #fff; 
}
::-moz-placeholder {
   color: #fff;
}
:-ms-input-placeholder {  
   color: #fff; 
}
input:focus, textarea:focus { 
   background-color: rgba(0, 0, 0, 0.2);
   -moz-box-shadow: 0 0 5px 1px rgba(255,255,255,.5);
   -webkit-box-shadow: 0 0 5px 1px rgba(255,255,255,.5);
   box-shadow: 0 0 5px 1px rgba(255,255,255,.5);
   overflow: hidden; 
}
:focus::-webkit-input-placeholder { color:transparent; }
:focus::-moz-placeholder { color:transparent; }
:focus::placeholder { color:transparent; }
 
/* Стили для кнопки отправить */
.contact-form__button {
    -moz-border-radius: 4px;
    -webkit-border-radius: 4px;
        border-radius: 4px;
    border: 1px solid #253737;
    background: #416b68;
    background: -webkit-gradient(linear, left top, left bottom, from(#6da5a3), to(#416b68));
        background: -webkit-linear-gradient(top, #f1f104, #3b3e40);
    background: -moz-linear-gradient(top,#f1f104, #3b3e40);
    background: -ms-linear-gradient(top,#f1f104, #3b3e40);
    background: -o-linear-gradient(top, #f1f104, #3b3e40);
    background-image: -ms-linear-gradient(top, #f1f104, #3b3e40);
    -webkit-border-radius: 6px;
    -moz-border-radius: 6px;
    border-radius: 6px;
    -webkit-box-shadow: rgba(255, 255, 255, 0.1) 0 1px 0, inset rgba(255,255,255,0.7) 0 1px 0;
    -moz-box-shadow: rgba(255,255,255,0.1) 0 1px 0, inset rgba(255,255,255,0.7) 0 1px 0;
    box-shadow: rgba(255,255,255,0.1) 0 1px 0, inset rgba(255,255,255,0.7) 0 1px 0;
    color: #e1e1e1;
    outline: none;
}
.contact-form__button:hover {
    border: 1px solid #253737;
    background: #416b68;
    background: -webkit-gradient(linear, left top, left bottom, from(#77b2b0), to(#416b68));
    background: -webkit-linear-gradient(top, #f1f104, #3b3e40);
    background: -moz-linear-gradient(top,#f1f104, #3b3e40);
    background: -ms-linear-gradient(top, #f1f104, #3b3e40);
    background: -o-linear-gradient(top, #f1f104, #3b3e40);
    background-image: -ms-linear-gradient(top, #f1f104, #3b3e40);
    color: #fff;
 }
.contact-form__button:active {
    margin-top:1px;
    border: 1px solid #333333;
    background: #ffCC00;
    background: -webkit-gradient(linear, left top, left bottom, from(#ffCC00), to(#ff6600));
    background: -webkit-linear-gradient(top, #ffcc00, #ff6600);
    background: -moz-linear-gradient(top, #ffcc00, #ff6600);
    background: -ms-linear-gradient(top, #ffcc00, #ff6600);
    background: -o-linear-gradient(top, #ffcc00, #ff6600);
    background-image: -ms-linear-gradient(top, #ffcc00 0%, #ff6600 100%);
    -webkit-box-shadow: rgba(255,255,255,0) 0 1px 0, inset rgba(255,255,255,0.7) 0 1px 0;
    -moz-box-shadow: rgba(255,255,255,0) 0 1px 0, inset rgba(255,255,255,0.7) 0 1px 0;
    box-shadow: rgba(255,255,255,0) 0 1px 0, inset rgba(255,255,255,0.7) 0 1px 0;
    color: #fff;
}
/* конец формы */
 
/** стили фона затемнения */
.overlay {
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 10000;
  visibility: hidden;
/* фон затемнения */
  background-color: rgba(0, 0, 0, 0.8);
  opacity: 0;
  position: fixed; /* фиксированное позиционирование */
/* трансформация прозрачности при открытии  */
  -webkit-transition: opacity .5s;
  -moz-transition: opacity .5s;
  -ms-transition: opacity .5s;
   -o-transition: opacity .5s;
   transition: opacity .5s;
}
.overlay:target {
  visibility: visible;
  opacity: 1;
}
/** стили модального блока */
.contact-form {
 top: 0;
 right: 0;
 left: 0;
 width: 50%;
 z-index: 10001;
/** полная прозрачность изначально */
 opacity: 0;
 display: block;
 visibility: hidden;
 position: absolute;
 text-align: center;
/* трансформация прозрачности при открытии  */
 -webkit-transition: opacity 500ms ease-in;
 -moz-transition: opacity 500ms ease-in;
 transition: opacity 500ms ease-in; 
}
.overlay:target+.contact-form{
  top: 5%;
  visibility: visible;
  opacity: 1;
  text-align: center;
}
/* планшет */
@media only screen and (min-width: 768px) and (max-width: 959px) {
    .contact-form {
       width: 95%;
    }
}
/* мобильный */
@media only screen and (min-width: 459px) and (max-width: 767px) {
    .contact-form {
       width:85%;  
    }
}
</style>
  <style>
   php { 
    text-decoration: none; /* Отменяем подчеркивание у ссылки */
   } 
  </style>
</head>
<body>
   

           <!-- Модальная форма -->
             <a href="#form1" class="overlay" id="form1"></a>

      <form id="form-contact" method="POST" action="./post/telegramform/php/send-message-to-telegram.php" class="contact-form" autocomplete="off" enctype="multipart/form-data">
      <?php 
  
    if(isset($_GET['action']) && $_GET['action']=="add"){ 
          
        $id=intval($_GET['id']); 
          
        if(isset($_SESSION['cart'][$id])){ 
              
            $_SESSION['cart'][$id]['quantity']++; 
              
        }else{ 
                        $link=mysqli_connect('localhost', 'root', '', 'userlistdb')
                        or die("Ошибка " . mysqli_error($link)); 
            $sql_s="SELECT * FROM products WHERE id={$id}"; 
            $query_s=mysqli_query($link, $sql_s); 
            if(mysqli_num_rows($query_s)!=0){ 
                $row_s=mysqli_fetch_array($query_s); 
                  
                $_SESSION['cart'][$row_s['id']]=array( 
                        "quantity" => 1, 
                        "price" => $row_s['price'] 
                    ); 
                  
                  
            }else{ 
                  
                $message="This product id it's invalid!"; 
                  
            } 
              
        } 
          
    } 
  
?>  
        <p class="contact-form__title"><h2 style="color: yellow;">Закажите обратный звонок, и мы свяжемся с Вами</h2><br></p>
        <p class="contact-form__message"></p>
          <div class="contact-form__input-wrapper contact-form__input-wrapper_name">
             
              <p style="color: white; text-align: left">Введите ваше имя</p>
            <input name="name" type="text" class="contact-form__input contact-form__input_name" tabindex="0"  required />
          </div>
          <div class="contact-form__input-wrapper contact-form__input-wrapper_phone">
              <p style="color: white; text-align: left">Введите ваш телефон</p>
          <input name="phone" type="tel" class="contact-form__input contact-form__input_phone" tabindex="0" placeholder="Введите ваш телефон"required />
          <div class="contact-form__input-wrapper contact-form__input-wrapper_email">
              <p style="color: white; text-align: left">Введите ваш email</p>
          <input name="email" type="email" class="contact-form__input contact-form__input_email" tabindex="0" placeholder="Введите ваш email"required />
              </div>
              
          <div class="contact-form__input-wrapper contact-form__input-wrapper_phone">
              <p style="color: white; text-align: left">Ваше сообщение </p>
          <input name="text" type="text" class="contact-form__input contact-form__input_text" tabindex="0"placeholder="Введите ваше сообщение">
          </div>
          
          <input type="hidden" name="nam" value="<?php echo $name?>" >
          <input type="hidden" name="price" value="<?php echo $price ?>" >
          
          <input name="theme" type="hidden" class="contact-form__input contact-form__input_theme"  value="ЗАКАЗ С САЙТА">
          <button type="submit" class="contact-form__button" style="width: 260px; height: 50px;"><h3>Отправить</h3></button>
      </form>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
    <script src="/telegramform/js/telegramform.js"></script>

         <!-- конец блока  формы-->
 </body></html>