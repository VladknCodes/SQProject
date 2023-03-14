const items_qs = [
      { number: 1,
            supplier: 'Supplier 1',
            product: 'Product 1',
            project: 'NPP "Project 1" / NPP "Project 2"',
            audit: '29.11.2021-03.12.2021',
            ncr: 24,
            ncrclosed: 16,
            progress: 67 },

      { number: 2,
            supplier: 'Supplier 2',
            product: 'Product 2',
            project: 'NPP "Project 1"',
            audit: '15.12.2021',
            ncr: 38,
            ncrclosed: 33,
            progress: 87 },

      { number: 3,
            supplier: 'Supplier 3',
            product: 'Product 3',
            project: 'NPP "Project 1" / NPP "Project 2"',
            audit: '18.04 -20.04.2022, 19.05 - 20.05.2022',
            ncr: 15,
            ncrclosed: 6,
            progress: 40 },

      { number: 4,
            supplier: 'Supplier 4',
            product: 'Product 4',
            project: 'NPP "Project 1"',
            audit: '24-25.03.2022',
            ncr: 17,
            ncrclosed: 15,
            progress: 88 },

      { number: 5,
            supplier: 'Supplier 5',
            product: 'Product 5',
            project: 'NPP "Project 1"',
            audit: '12-13.04.2022',
            ncr: 11,
            ncrclosed: 8,
            progress: 73 },

      { number: 6,
            supplier: 'Supplier 6',
            product: 'Product 6',
            project: 'NPP "Project 2"',
            audit: '11-13.06.2019',
            ncr: 59,
            ncrclosed: 58,
            progress: 98 },

      { number: 7,
            supplier: 'Supplier 7',
            product: 'Product 7',
            project: 'NPP "Project 2"',
            audit: '10.02.2022',
            ncr: 29,
            ncrclosed: 6,
            progress: 21 },

      { number: 8,
            supplier: 'Supplier 8',
            product: 'Product 8',
            project: 'NPP "Project 2"',
            audit: '12-14.10.2021',
            ncr: 18,
            ncrclosed: 17,
            progress: 94 },

      { number: 9,
            supplier: 'Supplier 9',
            product: 'Product 9',
            project: 'NPP "Project 1"',
            audit: '17-19.10.2022',
            ncr: 11,
            ncrclosed: 4,
            progress: 36 },

      { number: 10,
            supplier: 'Supplier 10',
            product: 'Product 10',
            project: 'NPP "Project 2"',
            audit: '11-13.09.2022',
            ncr: 33,
            ncrclosed: 15,
            progress: 45 },


];

document.querySelector('#table_pak tbody').innerHTML = items_qs.map(n => `
  <tr class="table_tr_as table_tr_link">
    <td class="table_th_td_as">${n.number}</td>
    <td class="table_th_td_as">${n.supplier}</td>
    <td class="table_th_td_as">${n.product}</td>
    <td class="table_th_td_as">${n.project}</td>
    <td class="table_th_td_as">${n.audit}</td>
    <td class="table_th_td_as">${n.ncr}</td>
    <td class="table_th_td_as">${n.ncrclosed}</td>
    <td class="table_th_td_as">${n.progress}</td>
  </tr>`).join('');
