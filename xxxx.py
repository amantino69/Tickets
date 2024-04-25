from bs4 import BeautifulSoup

html = '''<div class="ticket-article"><div class="ticket-article-item customer" data-id="29600" id="article-29600">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">Jean costa  <span class="text-muted">&lt;jean.costa@vivver.com.br&gt;</span></div>
      </div>
    
    
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">Para</div>
        <div class="article-meta-value flex contain-text">Crescer Tecnologia - N2</div>
      </div>
    
    
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar size-40 user-popover user-popover avatar--unique" style="background-position: -230.92135384537596px -181.03559744573184px;" data-id="38">
  
  Jc
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-29600" data-id="29600" data-height="1325.39" data-height-origin="560" style="height: 560px;">
          <div class="richtext-content" dir="auto"><div>Município: Volta Redonda - RJ<br>
</div><div>Módulo: Ambulatório</div><div>Versão: v24.01.20</div><div>Caminho: Ambulatório - Exportação de Produção de RAAS</div><div>Tipo: Incidência</div><div><br></div><div>Descrição do chamado:</div><div>Ao gerar o arquivo de exportação RAAS, foi identificado que a produção é exibida como produção estadual sendo que o cliente é gestão plena (municipal). Com isso, os arquivos que estão sendo gerados como "gestão estadual" ao invés de "municipal", não estão sendo identificadas / importadas no programa RAAS e o SIA está rejeitando a importação das produções geradas pelo Sistema Vivver, acarretando em perca de produção ao Município.</div><div><br></div><div>Desta forma solicita-se avaliação e resolução imediata, visto que tal incidência tem impedido as exportações de produções no cliente. Hoje são 5 unidades de CAPS e 3 Residências Terapêuticas pendentes de envio da produção.</div><div><br></div><div>Chamado URGÊNTE! As unidades estão sem o envio da produção ate o presente momento.</div><div><br></div><div>Segue em anexo:</div><div>•? &nbsp;?Arquivo gerado pelo sistema RAAS (novembro 2023 - Unidade CAPS Vila Esperança) - Com os dados corretos</div><div>•? &nbsp;?Arquivo gerado pelo sistema Vivver (janeiro - 2024 - Unidade CAPS AD) - Com os dados errados</div><div>É necessário que no cabeçalho possua a sequência correta aceita pelo SIA, informando SMS e o nome da unidade</div><div><br></div><div>Chamado "VOLREDON37717	[Volta Redonda-RJ][Ambulatório][Exportação de Produção RAAS] Dados do Estado está incorreto no arquivo RAAS"</div><div>
<img style="max-width:100%;width: 1000px;max-width: 100%;" src="/api/v1/ticket_attachment/8798/29600/18566?view=inline"><br>
</div><div><br></div><div>
<img style="max-width:100%;width: 1000px;max-width: 100%;" src="/api/v1/ticket_attachment/8798/29600/18567?view=inline"><br>
</div></div>
          <div class="textBubble-overflowContainer">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-web article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-web"></use></svg>
          web
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/29600"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-02-20T17:16:16.363Z" title="20/02/2024 14:16">20/02/2024</time></small></a>
</div><div class="ticket-article-item system" data-id="29619" id="article-29619">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">- </div>
      </div>
    
    
    
    
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">Assunto</div>
        <div class="article-meta-value flex contain-text">Encerramento automático</div>
      </div>
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar " style="background: white">
  <svg class="icon icon-logo "><use xlink:href="assets/images/icons.svg#icon-logo"></use></svg>
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-29619" data-id="29619">
          <div class="richtext-content" dir="auto">Este ticket fechará automaticamente em 10 dias caso não seja retornado.</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-note article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-note"></use></svg>
          nota
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/29619"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-02-20T18:48:02.319Z" title="20/02/2024 15:48">20/02/2024</time></small></a>
</div><div class="ticket-article-item agent" data-id="30324" id="article-30324">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">Filipe Carneiro</div>
      </div>
    
    
    
    
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar size-40 user-popover user-popover" style="background-image: url(api/v1/users/image/c88a5b3fa5607d83082d5a39b53fb488)" data-id="33" data-initials="FC">
  
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30324" data-id="30324">
          <div class="richtext-content" dir="auto"><p>É necessário preencher esses dados no sistema e fazer nova exportação da produção RAAS. Eles são obrigatórios.</p><br><div><img src="/api/v1/ticket_attachment/8798/30324/18958?view=inline" style="max-width:100%;width: 1000px;max-width: 100%;"></div></div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-note article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-note"></use></svg>
          nota
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30324"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-06T20:40:29.547Z" title="06/03/2024 17:40">06/03/2024</time></small></a>
</div><div class="ticket-article-item system" data-id="30325" id="article-30325">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">- </div>
      </div>
    
    
    
    
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">Assunto</div>
        <div class="article-meta-value flex contain-text">Encerramento automático</div>
      </div>
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar " style="background: white">
  <svg class="icon icon-logo "><use xlink:href="assets/images/icons.svg#icon-logo"></use></svg>
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30325" data-id="30325">
          <div class="richtext-content" dir="auto">Este ticket fechará automaticamente em 10 dias caso não seja retornado.</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-note article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-note"></use></svg>
          nota
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30325"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-06T20:40:30.475Z" title="06/03/2024 17:40">06/03/2024</time></small></a>
</div><div class="ticket-article-item customer" data-id="30355" id="article-30355">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">Jean costa  <span class="text-muted">&lt;jean.costa@vivver.com.br&gt;</span></div>
      </div>
    
    
    
    
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar size-40 user-popover user-popover avatar--unique" style="background-position: -230.92135384537596px -181.03559744573184px;" data-id="38">
  
  Jc
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30355" data-id="30355">
          <div class="richtext-content" dir="auto">Bom dia!<br><br>Solicitado validação no cliente.</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-web article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-web"></use></svg>
          web
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30355"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-07T12:54:09.872Z" title="07/03/2024 09:54">07/03/2024</time></small></a>
</div><div class="ticket-article-item system" data-id="30356" id="article-30356">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">- </div>
      </div>
    
    
    
    
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">Assunto</div>
        <div class="article-meta-value flex contain-text">Encerramento automático</div>
      </div>
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar " style="background: white">
  <svg class="icon icon-logo "><use xlink:href="assets/images/icons.svg#icon-logo"></use></svg>
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30356" data-id="30356">
          <div class="richtext-content" dir="auto">Este ticket fechará automaticamente em 10 dias caso não seja retornado.</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-note article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-note"></use></svg>
          nota
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30356"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-07T12:54:10.591Z" title="07/03/2024 09:54">07/03/2024</time></small></a>
</div><div class="ticket-article-item customer" data-id="30391" id="article-30391">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">Jean costa  <span class="text-muted">&lt;jean.costa@vivver.com.br&gt;</span></div>
      </div>
    
    
    
    
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar size-40 user-popover user-popover avatar--unique" style="background-position: -230.92135384537596px -181.03559744573184px;" data-id="38">
  
  Jc
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30391" data-id="30391">
          <div class="richtext-content" dir="auto">Erro 500 ao tentar inserir as informações.<div>
<img style="max-width:100%;width: 1000px;max-width: 100%;" src="/api/v1/ticket_attachment/8798/30391/18984?view=inline"><br>
</div></div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        
  <div class="attachments attachments--list">
    <svg class="icon icon-paperclip "><use xlink:href="assets/images/icons.svg#icon-paperclip"></use></svg>
    <div class="attachments-title">1 Arquivo(s) Anexado</div>
    
      
        
        <a class="attachment attachment--preview " href="api/v1/ticket_attachment/8798/30391/18983?disposition=attachment" data-type="attachment" data-preview-url="api/v1/ticket_attachment/8798/30391/18983?view=preview" data-id="18983" download="">
          <div class="attachment-icon js-preview">
          
            <svg class="icon icon-file-unknown "><use xlink:href="assets/images/icons.svg#icon-file-unknown"></use></svg>
          
          </div>
          <div class="attachment-text">
            <span class="attachment-name u-highlight">Não_é_permitido_alterar_as_informações_solicitadas_no_Print (1).mp4</span>
            <div class="attachment-size">426 KB</div>
          </div>
          
        </a>
      
    
  </div>


      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-web article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-web"></use></svg>
          web
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30391"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-07T17:51:35.923Z" title="07/03/2024 14:51">07/03/2024</time></small></a>
</div><div class="ticket-article-item agent" data-id="30435" id="article-30435">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">Filipe Carneiro</div>
      </div>
    
    
    
    
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar size-40 user-popover user-popover" style="background-image: url(api/v1/users/image/c88a5b3fa5607d83082d5a39b53fb488)" data-id="33" data-initials="FC">
  
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30435" data-id="30435">
          <div class="richtext-content" dir="auto">Fizemos a alteração direto no banco oficial, para que seja feita a exporação de produção, estamos verificando sobre o erro na edição dos registros.</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-note article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-note"></use></svg>
          nota
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30435"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-08T21:03:13.787Z" title="08/03/2024 18:03">08/03/2024</time></small></a>
</div><div class="ticket-article-item system" data-id="30436" id="article-30436">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">- </div>
      </div>
    
    
    
    
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">Assunto</div>
        <div class="article-meta-value flex contain-text">Encerramento automático</div>
      </div>
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar " style="background: white">
  <svg class="icon icon-logo "><use xlink:href="assets/images/icons.svg#icon-logo"></use></svg>
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30436" data-id="30436">
          <div class="richtext-content" dir="auto">Este ticket fechará automaticamente em 10 dias caso não seja retornado.</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-note article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-note"></use></svg>
          nota
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30436"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-08T21:03:15.001Z" title="08/03/2024 18:03">08/03/2024</time></small></a>
</div><div class="ticket-article-item customer" data-id="30445" id="article-30445">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">Jean costa  <span class="text-muted">&lt;jean.costa@vivver.com.br&gt;</span></div>
      </div>
    
    
    
    
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar size-40 user-popover user-popover avatar--unique" style="background-position: -230.92135384537596px -181.03559744573184px;" data-id="38">
  
  Jc
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30445" data-id="30445">
          <div class="richtext-content" dir="auto"><span style="color:rgb(236, 236, 236);">Bom dia!<br><br>Como o problema ainda não foi totalmente resolvido, manteremos o ticket em aberto.<br><br></span><div>A informação sobre a correção realizada no banco oficial foi enviada para Irai validar.<span style="color:rgb(236, 236, 236);"><br></span>
</div></div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-web article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-web"></use></svg>
          web
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30445"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-11T12:53:56.031Z" title="11/03/2024 09:53">11/03/2024</time></small></a>
</div><div class="ticket-article-item customer" data-id="30464" id="article-30464">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">Jean costa  <span class="text-muted">&lt;jean.costa@vivver.com.br&gt;</span></div>
      </div>
    
    
    
    
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar size-40 user-popover user-popover avatar--unique" style="background-position: -230.92135384537596px -181.03559744573184px;" data-id="38">
  
  Jc
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30464" data-id="30464">
          <div class="richtext-content" dir="auto">Boa tarde!<br><br>Após testes realizados pelo Irai, informou que o arquivo ainda continua com erro. Segue em anexo.</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        
  <div class="attachments attachments--list">
    <svg class="icon icon-paperclip "><use xlink:href="assets/images/icons.svg#icon-paperclip"></use></svg>
    <div class="attachments-title">2 Arquivo(s) Anexado</div>
    
      
        
        <a class="attachment attachment--preview " href="api/v1/ticket_attachment/8798/30464/19028?disposition=attachment" data-type="attachment" data-preview-url="api/v1/ticket_attachment/8798/30464/19028?view=preview" data-id="19028" download="">
          <div class="attachment-icon js-preview">
          
            <svg class="icon icon-file-unknown "><use xlink:href="assets/images/icons.svg#icon-file-unknown"></use></svg>
          
          </div>
          <div class="attachment-text">
            <span class="attachment-name u-highlight">AARAAS (2).FEV</span>
            <div class="attachment-size">60 KB</div>
          </div>
          
        </a>
      
    
      
        
        <a class="attachment attachment--preview " href="api/v1/ticket_attachment/8798/30464/19029?disposition=attachment" data-type="attachment" data-preview-url="api/v1/ticket_attachment/8798/30464/19029?view=preview" data-id="19029" download="">
          <div class="attachment-icon js-preview">
          
            <svg class="icon icon-file-unknown "><use xlink:href="assets/images/icons.svg#icon-file-unknown"></use></svg>
          
          </div>
          <div class="attachment-text">
            <span class="attachment-name u-highlight">AA314790_PROTOCOLO (2).FEV</span>
            <div class="attachment-size">4 KB</div>
          </div>
          
        </a>
      
    
  </div>


      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-web article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-web"></use></svg>
          web
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30464"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-11T17:32:35.960Z" title="11/03/2024 14:32">11/03/2024</time></small></a>
</div><div class="ticket-article-item agent" data-id="30543" id="article-30543">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">Filipe Carneiro</div>
      </div>
    
    
    
    
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar size-40 user-popover user-popover" style="background-image: url(api/v1/users/image/c88a5b3fa5607d83082d5a39b53fb488)" data-id="33" data-initials="FC">
  
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30543" data-id="30543">
          <div class="richtext-content" dir="auto">Favor validar.</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-note article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-note"></use></svg>
          nota
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30543"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-13T13:28:20.889Z" title="13/03/2024 10:28">13/03/2024</time></small></a>
</div><div class="ticket-article-item system" data-id="30544" id="article-30544">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">- </div>
      </div>
    
    
    
    
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">Assunto</div>
        <div class="article-meta-value flex contain-text">Encerramento automático</div>
      </div>
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar " style="background: white">
  <svg class="icon icon-logo "><use xlink:href="assets/images/icons.svg#icon-logo"></use></svg>
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30544" data-id="30544">
          <div class="richtext-content" dir="auto">Este ticket fechará automaticamente em 10 dias caso não seja retornado.</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-note article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-note"></use></svg>
          nota
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30544"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-13T13:28:21.659Z" title="13/03/2024 10:28">13/03/2024</time></small></a>
</div><div class="ticket-article-item customer" data-id="30545" id="article-30545">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">Jean costa  <span class="text-muted">&lt;jean.costa@vivver.com.br&gt;</span></div>
      </div>
    
    
    
    
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar size-40 user-popover user-popover avatar--unique" style="background-position: -230.92135384537596px -181.03559744573184px;" data-id="38">
  
  Jc
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30545" data-id="30545">
          <div class="richtext-content" dir="auto"><p>Foi solicitado ao Irai que realize os testes e a validação do arquivo.</p><p>Ficamos no aguardo do retorno</p></div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-web article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-web"></use></svg>
          web
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30545"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-13T13:32:59.444Z" title="13/03/2024 10:32">13/03/2024</time></small></a>
</div><div class="ticket-article-item system" data-id="30546" id="article-30546">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">- </div>
      </div>
    
    
    
    
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">Assunto</div>
        <div class="article-meta-value flex contain-text">Encerramento automático</div>
      </div>
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar " style="background: white">
  <svg class="icon icon-logo "><use xlink:href="assets/images/icons.svg#icon-logo"></use></svg>
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30546" data-id="30546">
          <div class="richtext-content" dir="auto">Este ticket fechará automaticamente em 10 dias caso não seja retornado.</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-note article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-note"></use></svg>
          nota
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30546"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-13T13:33:00.187Z" title="13/03/2024 10:33">13/03/2024</time></small></a>
</div><div class="ticket-article-item system" data-id="30575" id="article-30575">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">- </div>
      </div>
    
    
    
    
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">Assunto</div>
        <div class="article-meta-value flex contain-text">Encerramento automático</div>
      </div>
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar " style="background: white">
  <svg class="icon icon-logo "><use xlink:href="assets/images/icons.svg#icon-logo"></use></svg>
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30575" data-id="30575">
          <div class="richtext-content" dir="auto">Este ticket fechará automaticamente em 10 dias caso não seja retornado.</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-note article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-note"></use></svg>
          nota
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30575"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-13T20:14:21.315Z" title="13/03/2024 17:14">13/03/2024</time></small></a>
</div><div class="ticket-article-item customer" data-id="30629" id="article-30629">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">Jean costa  <span class="text-muted">&lt;jean.costa@vivver.com.br&gt;</span></div>
      </div>
    
    
    
    
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar size-40 user-popover user-popover avatar--unique" style="background-position: -230.92135384537596px -181.03559744573184px;" data-id="38">
  
  Jc
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30629" data-id="30629">
          <div class="richtext-content" dir="auto">Arquivo continua com erro. Gerando como órgão estatual.</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-web article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-web"></use></svg>
          web
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30629"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-03-21T13:12:43.532Z" title="21/03/2024 10:12">21/03/2024</time></small></a>
</div><div class="ticket-article-item customer" data-id="30769" id="article-30769">


<div class="article-meta-clip top">
  <div class="article-content-meta top hide">
    <div class="article-meta top">
    
      <div class="horizontal article-meta-row">
        <div class="article-meta-key u-textTruncate">De</div>
        <div class="article-meta-value flex contain-text">Jean costa  <span class="text-muted">&lt;jean.costa@vivver.com.br&gt;</span></div>
      </div>
    
    
    
    
    
      
    </div>
  </div>
</div>

<div class="article-content">
  
  
  
  <div class="js-avatar"><span class="avatar size-40 user-popover user-popover avatar--unique" style="background-position: -230.92135384537596px -181.03559744573184px;" data-id="38">
  
  Jc
</span>
</div>
  <div class="bubble-gap">
    <div class="internal-border">
      <div class="textBubble">
        <div class="bubble-arrow"></div>
        <div class="textBubble-content" id="article-content-30769" data-id="30769">
          <div class="richtext-content" dir="auto">Não é possível alterar tais informações assim como solicitado e mostrado no anexo Print Resolução. Além disso, vale ressaltar que o órgão de destino já consta como Municipal, entretanto, no arquivo gerado (RAAS) está sendo informado como Estadual ao invés de Municipal. Assim como foi mostrado nos anexos anteriores, é necessário que o arquivo gerado no Vivver conste o CNES e nome da unidade (print do arquivo RAAS anexado anteriormente).</div>
          <div class="textBubble-overflowContainer hide">
            <div class="btn btn--text js-toggleFold">Ver mais</div>
          </div>
        </div>
        

      </div>
    </div>
  </div>
</div>
<div class="article-meta-clip bottom">
  <div class="article-content-meta bottom hide">
    <div class="article-meta bottom">
      <div class="horizontal article-meta-row">
        <div class="article-meta-key">Canal</div>
        <div class="article-meta-value">
          
          <svg class="icon icon-web article-meta-icon"><use xlink:href="assets/images/icons.svg#icon-web"></use></svg>
          web
          <div class="article-meta-links">
          
            
            
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="js-article-actions"><div class="article-content article-actions horizontal">
  
</div>
</div>

<a href="http://https://ticket.crescer.net//#ticket/zoom/8798/30769"><small class="task-subline"><time class="humanTimeFromNow " datetime="2024-04-02T14:01:15.007Z" title="02/04/2024 11:01">7 horas 46 minutos atrás</time></small></a>
</div></div>'''


# Supondo que 'html' é a sua string HTML
soup = BeautifulSoup(html, 'html.parser')

# Encontra a primeira div com a classe 'ticket-article-item customer'
div = soup.find('div', class_='ticket-article-item')


# Encontra todas as divs com a classe 'ticket-article-item customer'
divs = soup.find_all('div', class_='ticket-article-item')

# Obtém o último elemento da lista
ultimo_elemento = divs[-1].text
penultimo_elemento = divs[-2].text
antipenultimo_elemento = divs[-3].text

print("Último elemento = ", ultimo_elemento)
print("penultimo_elemento = ", penultimo_elemento)
print("antipenultimo_elemento = ", antipenultimo_elemento)