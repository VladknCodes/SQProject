{/* Функция установки фона ячейки в зависимости от значение */}
var classdata = "table_react table_th_td_as"
function createMarkup(period) {
  if (period === "") classdata = "table_react table_th_td_as"
  else classdata = "table_react table_th_td_as table_react_color"
}
{/* ---------------------------- */}



{/* Асинхронная функция отправки сетевого запроса на скачивание данных из файла и декодирование ответа в формате JSON  */}
async function get_user_name(urldata) {
    
  let response = await fetch(urldata);
  var user = await response.json();
  
  return user;

}
{/* ---------------------------- */}



{/* Рендеринг элементов в асинхронной функции */}
(async () => {
  
  console.log(await get_user_name('/static/js/paks_ap.json'));
  ReactDOM.createRoot(document.getElementById("app1")).render(<App data={await get_user_name('/static/js/paks_ap.json')} />);
  
})();


(async () => {
  
  console.log(await get_user_name('/static/js/akkuyu_ap.json'));
  ReactDOM.createRoot(document.getElementById("app2")).render(<App data={await get_user_name('/static/js/akkuyu_ap.json')} />);
  
})();


(async () => {
  
  console.log(await get_user_name('/static/js/eldabaa_ap.json'));
  ReactDOM.createRoot(document.getElementById("app3")).render(<App data={await get_user_name('/static/js/eldabaa_ap.json')} />);
  
})();
{/* ---------------------------- */}



{/* Рендеринг элементов списка */}
function App (props) {
  let res = props.data.map(function(item)
  {
    return <tr key={item.id} class="table_tr_as table_tr_link">
      <td class="table_th_td_as">{item.product}</td>
      <td class="table_react table_th_td_as">{item.LTTA}</td>

      <td dangerouslySetInnerHTML={createMarkup(item.Jan2023)} className={classdata}>{item.Jan2023}</td>
      <td dangerouslySetInnerHTML={createMarkup(item.Feb2023)} className={classdata}>{item.Feb2023}</td>
      <td dangerouslySetInnerHTML={createMarkup(item.Mar2023)} className={classdata}>{item.Mar2023}</td>
      <td dangerouslySetInnerHTML={createMarkup(item.Apr2023)} className={classdata}>{item.Apr2023}</td>
      <td dangerouslySetInnerHTML={createMarkup(item.May2023)} className={classdata}>{item.May2023}</td>
      <td dangerouslySetInnerHTML={createMarkup(item.Jun2023)} className={classdata}>{item.Jun2023}</td>
      <td dangerouslySetInnerHTML={createMarkup(item.Jul2023)} className={classdata}>{item.Jul2023}</td>
      <td dangerouslySetInnerHTML={createMarkup(item.Aug2023)} className={classdata}>{item.Aug2023}</td>
      <td dangerouslySetInnerHTML={createMarkup(item.Sep2023)} className={classdata}>{item.Sep2023}</td>
      <td dangerouslySetInnerHTML={createMarkup(item.Oct2023)} className={classdata}>{item.Oct2023}</td>
      <td dangerouslySetInnerHTML={createMarkup(item.Nov2023)} className={classdata}>{item.Nov2023}</td>
      <td dangerouslySetInnerHTML={createMarkup(item.Dec2023)} className={classdata}>{item.Dec2023}</td>
      <td dangerouslySetInnerHTML={createMarkup(item._24)} className={classdata}>{item._24}</td>

    </tr>;

  });

  return <table class="table_as">

    <thead class="table_thead_as">
				  <tr class="table_tr_as">
            <th class="table_th_td_as">Priduct</th>
            <th class="table_th_td_as" width="20">LTTA</th>
            <th class="table_th_td_as" width="20">Jan 2023</th>
            <th class="table_th_td_as" width="20">Feb 2023</th>
            <th class="table_th_td_as" width="20">Mar 2023</th>
            <th class="table_th_td_as" width="20">Apr 2023</th>
            <th class="table_th_td_as" width="20">May 2023</th>
            <th class="table_th_td_as" width="20">Jun 2023</th>
            <th class="table_th_td_as" width="20">Jul 2023</th>
            <th class="table_th_td_as" width="20">Aug 2023</th>
            <th class="table_th_td_as" width="20">Sep 2023</th>
            <th class="table_th_td_as" width="20">Oct 2023</th>
            <th class="table_th_td_as" width="20">Nov 2023</th>
            <th class="table_th_td_as" width="20">Dec 2023</th>
            <th class="table_th_td_as" width="20">2024</th>
          </tr>
    </thead>

    <tbody class="table_tbody_as">
      {res}
    </tbody>
  </table>;

}
{/* ---------------------------- */}
