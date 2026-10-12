import './style.css';

document.querySelector('#app').innerHTML = `
  <main class="dashboard">
    <p class="eyebrow">FINTECH CORE</p>
    <h1>Dashboard financeiro</h1>
    <p class="intro">Frontend inicial do ecossistema de microsserviços.</p>
    <section class="status-card" aria-live="polite">
      <span class="status-dot"></span>
      <div>
        <h2>Frontend ativo</h2>
        <p>O ambiente de desenvolvimento está funcionando.</p>
      </div>
    </section>
  </main>
`;
