describe("Check lag between server and client", () => {
  it("expects to be less then 1 second", () => {
    cy.intercept("/").as("apiRequest");
    cy.visit("/");
    
    // Write message in input field and send it to the server
    cy.get("[id=messageText]").type("Hello, World!");
    cy.wait(200);
    cy.get("[id=sendText]").click();

    // Calculate time when send the message
    const start = performance.now();

    cy.wait("@apiRequest").then(() => {
      // Calculate lag between client and server
      const endTime = performance.now();
      const lag = endTime - start;

      // Log lag between server and client
      cy.log(`Lag between client and server: ${lag.toFixed(2)} ms`);
      // Except lag be less or equal to 1 second(1000 ms)
      expect(lag).lessThan(1000);

      // Update count of messages
      cy.get("[id=updateMessages]").click();
    });
  });
});

describe("Check whether messages are saved after reconnect", () => {
  it("closes connection with server and reconnect", () => {
    cy.visit("/");

    // Send message in chat
    const sendMessage = (message) => {
      cy.get("[id=messageText]").type(message);
      cy.wait(200);
      cy.get("[id=sendText]").click();
    };

    sendMessage("Test message 1");
    sendMessage("Test message 2");
    sendMessage("Test message 3");

    // Get messages sent in chat in order to check after reloading page
    const getMessages = () => {
      const messages = [];
      cy.get("[id=messages]")
        .children()
        .should("have.length.greaterThan", 0)
        .each((elem) => messages.push(elem.text()));

      return messages;
    };

    // Save messages before reloading
    const messagesBeforeReload = getMessages();
    cy.reload();
    // Save messages after reloading
    const messageAfterReload = getMessages();

    // Check whether messages before and after reloading are equal
    cy.wait(0).then(() => {
      expect(messageAfterReload).to.deep.equal(messagesBeforeReload);
    });
  });
});
