/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { LossService } from './loss.service';

describe('Service: Loss', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [LossService]
    });
  });

  it('should ...', inject([LossService], (service: LossService) => {
    expect(service).toBeTruthy();
  }));
});
