describe('Plans page', () => {
  beforeEach(() => {
    cy.server()
    cy.route('GET', '/plans?zip_code=*').as('getPlans')
  })

  it('displays plans for valid zip codes', () => {
    const zipCode = '75229'

    cy.visit(`/plans/${zipCode}`)

    cy.get('svg[data-icon=loading-spinner]')

    cy.wait('@getPlans').should((xhr) => {
      expect(xhr.status).to.equal(200)
      expect(xhr.response.body).to.be.an('array').that.is.not.empty
    })

    cy.get('.plan-card:first').should(($div) => {
      expect($div.find('p:contains(low)')).to.have.class('cursor-pointer')
      expect($div.find('p:contains(med)')).to.not.have.class('cursor-pointer')
      expect($div.find('p:contains(high)')).to.have.class('cursor-pointer')
    })

    cy.get('.plan-card').first().contains('low').click()

    cy.get('.plan-card:first').should(($div) => {
      expect($div.find('p:contains(low)')).to.not.have.class('cursor-pointer')
      expect($div.find('p:contains(med)')).to.have.class('cursor-pointer')
      expect($div.find('p:contains(high)')).to.have.class('cursor-pointer')
    })

    cy.get('.plan-card').first().contains('high').click()

    cy.get('.plan-card:first').should(($div) => {
      expect($div.find('p:contains(low)')).to.have.class('cursor-pointer')
      expect($div.find('p:contains(med)')).to.have.class('cursor-pointer')
      expect($div.find('p:contains(high)')).to.not.have.class('cursor-pointer')
    })

    cy.get('#select-term').select('1')
    cy.get('#select-term').select('all')
    cy.get('#input-renewable').check()
    cy.get('#input-stars').last().click()
  })
})
