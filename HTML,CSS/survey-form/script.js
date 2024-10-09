it('should verify that the selected code is within the open file', function() {
    expect(openFile).toContain(selectedCode);
  });
  
  it('should verify that the selected code is within a valid HTML tag', function() {
    expect(selectedCode).toMatch(/<[\w\s\/=":.\-]+>/);
  });
  
  it('should verify that the selected code is within a valid JavaScript code block', function() {
    expect(selectedCode).toMatch(/```[\w\s\S]+```/);
  });